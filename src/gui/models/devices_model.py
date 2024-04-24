from PyQt5.QtCore import QObject, pyqtSignal


class DeviceModel(QObject):

    def __init__(self) -> None:
        super().__init__()
        self._device_id = ''
        self._model = ''
        self._android_version = ''
    
    def get_device_info(self) -> dict:
        return {
            'device_id': self.device_id,
            'model': self.model,
            'android_version': self.android_version,
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


class DevicesModel(QObject):

    device_added = pyqtSignal(dict)
    device_removed = pyqtSignal(str)

    def __init__(self) -> None:
        super().__init__()
        self._devices = {}
    
    def add_device(self, device_id: str, model: str, android_version: str) -> None:
        device = DeviceModel()
        device.device_id = device_id
        device.model = model
        device.android_version = android_version
        self._devices[device_id] = device
        self.device_added.emit(device.get_device_info())
    
    def remove_device(self, device_id: str) -> None:
        del self._devices[device_id]
        self.device_removed.emit(device_id)
    
    def get_devices(self) -> dict:
        devices = {}
        for device_id, device in self._devices.items():
            devices[device_id] = device.get_device_info()
        return devices
    
    def get_device(self, device_id: str) -> dict:
        return self._devices[device_id].get_device_info()
    
    def get_device_model(self, device_id: str) -> str:
        return self._devices[device_id].model
    
    def get_device_android_version(self, device_id: str) -> str:
        return self._devices[device_id].android_version
    
    def get_device_id(self, device_id: str) -> str:
        return self._devices[device_id].device_id
    