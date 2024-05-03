from PyQt5.QtCore import QObject, pyqtSignal


class DeviceModel(QObject):
    def __init__(self) -> None:
        super().__init__()
        self._device_id = None
        self._model = None
        self._android_version = None
        self._connection_type = None
        self._index = None

    def get_device_info(self) -> dict:
        return {
            'device_id': self.device_id,
            'model': self.model,
            'android_version': self.android_version,
            'connection_type': self.connection_type,
            'index': self.index,
        }

    @property
    def device_id(self) -> str:
        return self._device_id

    @device_id.setter
    def device_id(self, value: str) -> None:
        self._device_id = value

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = value

    @property
    def android_version(self) -> str:
        return self._android_version

    @android_version.setter
    def android_version(self, value: str) -> None:
        self._android_version = value

    @property
    def connection_type(self) -> str:
        return self._connection_type

    @connection_type.setter
    def connection_type(self, value: str) -> None:
        self._connection_type = value

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int) -> None:
        self._index = value


class DevicesModel(QObject):

    device_added = pyqtSignal(dict)
    device_removed = pyqtSignal(dict)

    def __init__(self) -> None:
        super().__init__()
        self._devices: dict[str, DeviceModel] = {}

    def add_device(
        self,
        device_id: str,
        model: str,
        android_version: str,
        connection_type: str,
    ) -> None:
        device = DeviceModel()
        device.device_id = device_id
        device.model = model
        device.android_version = android_version
        device.connection_type = connection_type
        device_index = len(self._devices)
        device.index = device_index
        self._devices[device_id] = device
        self.device_added.emit(device.get_device_info())

    def remove_device(self, device_id: str) -> None:
        device_info = self._devices[device_id].get_device_info()
        del self._devices[device_id]
        self.device_removed.emit(device_info)

    def get_devices(self) -> dict:
        devices = {}
        for device_id, device in self._devices.items():
            devices[device_id] = device.get_device_info()
        return devices

    def get_device(self, device_id: str) -> dict:
        return self._devices[device_id].get_device_info()
