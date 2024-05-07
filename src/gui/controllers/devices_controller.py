import _thread as thread
import time

from PyQt5.QtCore import QObject, pyqtSignal

from src.gui.models.devices_model import DevicesModel
from src.gui.services.adb_service import ADBService


class DevicesController(QObject):

    device_added = pyqtSignal(dict)
    device_removed = pyqtSignal(dict)
    show_popup_signal = pyqtSignal(str, str)

    def __init__(
        self, devices_model: DevicesModel, adb_service: ADBService
    ) -> None:
        super().__init__()
        self._devices_model = devices_model
        self._adb_service = adb_service
        self._devices_model.device_added.connect(self._emit_device_added)
        self._devices_model.device_removed.connect(self._emit_device_removed)

    def _emit_device_added(self, device_info: dict) -> None:
        self.device_added.emit(device_info)

    def _emit_device_removed(self, device_id: str) -> None:
        self.device_removed.emit(device_id)

    def _add_connected_devices_to_model(self) -> None:
        devices_id = self._adb_service.get_id_from_connected_devices()
        for device_id in devices_id:

            if self._is_device_already_in_model(device_id):
                continue

            device_info = self._adb_service.get_device_info(device_id)
            connection_type = self._adb_service.get_device_connection_type(
                device_id
            )
            self._devices_model.add_device(
                device_id,
                device_info['model'],
                device_info['android_version'],
                connection_type,
            )

    def _is_device_already_in_model(
        self, device_id: str
    ) -> bool:   # TODO:  mover para o model
        return device_id in self._devices_model.get_devices().keys()

    def _remove_devices_from_model(self) -> None:
        devices_id = self._adb_service.get_id_from_connected_devices()
        for device_id in list(self._devices_model.get_devices().keys()):
            if device_id not in devices_id:
                self._devices_model.remove_device(device_id)

    def _watch_devices(self) -> None:
        while True:
            self._add_connected_devices_to_model()
            self._remove_devices_from_model()
            time.sleep(2)

    def watch_devices(self) -> None:
        thread.start_new_thread(self._watch_devices, ())

    def change_devices_connection_to_wifi(self, devices_id: str) -> None:
        devices_id_list = devices_id.split('\n')
        for device_id in devices_id_list:
            self._adb_service.connect_usb_device_over_wifi(device_id)

    def connect_devices_with_ip_address(self, devices_ip: str) -> None:
        devices_ip_list = devices_ip.split('\n')
        devices_not_connected = []
        for device_ip in devices_ip_list:
            if not self._adb_service.connect_device_with_ip_address(device_ip):
                devices_not_connected.append(device_ip)

        if devices_not_connected:
            devices_not_connected_str = '\n'.join(devices_not_connected)
            self.show_popup_signal.emit(
                'Dispositivos não conectados',
                f'Os seguintes dispositivos não foram conectados: {devices_not_connected_str}',
            )

    def disconnect_device(self, device_id: str) -> None:
        self._adb_service.disconnect_device(device_id)
