import os


class ADBService:
    def __init__(self, adb_executable_path: str) -> None:
        self._adb_executable_path = ''
        self.adb_executable_path = adb_executable_path

    @property
    def adb_executable_path(self) -> str:
        return self._adb_executable_path

    @adb_executable_path.setter
    def adb_executable_path(self, value) -> None:
        if not os.path.exists(value):
            raise FileNotFoundError(f'File not found in path: {value}')
        self._adb_executable_path = value

    def get_id_from_connected_devices(self) -> list:
        """
        Método responsável por retornar a lista de dispositivos conectados.

        Returns:
            list: Lista de dispositivos conectados.
        """
        cmd = f'{self.adb_executable_path} devices'
        result = os.popen(cmd).readlines()
        devices_id = []
        for line in result:
            if '\tdevice' in line:
                devices_id.append(line.split('\t')[0])
        return devices_id

    def get_device_info(self, device_id: str) -> dict:
        """
        Método responsável por retornar as informações do dispositivo.

        Args:
            device_id (str): ID do dispositivo.

        Returns:
            dict: Dicionário com as informações do dispositivo.
        """
        cmd = f'{self.adb_executable_path} -s {device_id} shell getprop ro.product.model'
        result = os.popen(cmd).readlines()
        model = result[0].strip()
        cmd = f'{self.adb_executable_path} -s {device_id} shell getprop ro.build.version.release'
        result = os.popen(cmd).readlines()
        android_version = result[0].strip()
        data = {'model': model, 'android_version': android_version}
        return data

    def get_only_usb_devices(self) -> list:
        """
        Método responsável por retornar a lista de dispositivos USB conectados.
        Dispositivos conectados via Wi-Fi não são retornados.

        Returns:
            list: Lista de dispositivos USB conectados.
        """
        devices_id = self.get_id_from_connected_devices()
        usb_devices = []
        for device_id in devices_id:
            if 'emulator' not in device_id and '.' not in device_id:
                usb_devices.append(device_id)
        return usb_devices

    def connect_device_with_ip_address(self, device_ip: str) -> bool:
        """
        Método responsável por conectar um dispositivo via Wi-Fi.

        Args:
            device_ip (str): IP do dispositivo.

        Returns:
            str: ID do dispositivo.
        """
        cmd = f'{self.adb_executable_path} connect {device_ip}'
        result = os.popen(cmd).readlines()
        if 'connected' in result[0]:
            return True
        else:
            return False

    def disconnect_emulator(self, device_ip: str) -> bool:
        """
        Método responsável por desconectar um dispositivo via Wi-Fi.

        Args:
            device_ip (str): IP do dispositivo.

        Returns:
            bool: True se desconectar, False se não desconectar.
        """
        cmd = f'{self.adb_executable_path} disconnect {device_ip}'
        result = os.popen(cmd).readlines()
        if 'disconnected' in result[0]:
            return True
        else:
            return False

    def get_usb_device_ip_address(self, device_id: str) -> str | None:
        """
        Método responsável por retornar o endereço IP de um dispositivo USB.

        Args:
            device_id (str): ID do dispositivo.

        Returns:
            str: Endereço IP do dispositivo.
        """
        cmd = f'{self.adb_executable_path} -s {device_id} shell ip -f inet addr show wlan0'
        result = os.popen(cmd).readlines()
        for line in result:
            # remove espaços em branco
            line = line.strip()
            if 'inet' in line:
                return line.split(' ')[1].split('/')[0]
        return None

    def restart_adb_to_tcp_mode(self) -> bool:
        """
        Método responsável por reiniciar o ADB em modo TCP.

        Returns:
            bool: True se reiniciar, False se não reiniciar.
        """
        cmd = f'{self.adb_executable_path} tcpip 5555'
        result = os.popen(cmd).readlines()
        if 'restarting in TCP mode port: 5555' in result[0]:
            return True
        else:
            return False

    def connect_usb_device_over_wifi(self, device_id: str) -> bool:
        """
        Método responsável por conectar um dispositivo USB via Wi-Fi.

        Args:
            device_id (str): ID do dispositivo.

        Returns:
            bool: True se conectar, False se não conectar.
        """
        if not self.restart_adb_to_tcp_mode():
            return False

        device_ip = self.get_usb_device_ip_address(device_id)
        if device_ip is None:
            return False

        return self.connect_device_with_ip_address(device_ip)

    def is_app_installed(self, device_id: str, app_package: str) -> bool:
        """
        Método responsável por verificar se um app está instalado no dispositivo.

        Args:
            device_id (str): ID do dispositivo.
            app_package (str): Nome do pacote do app.

        Returns:
            bool: True se o app está instalado, False se não está instalado.
        """
        cmd = (
            f'{self.adb_executable_path} -s {device_id} shell pm list packages'
        )
        result = os.popen(cmd).readlines()
        for line in result:
            if app_package in line:
                return True
        return False

    def install_app(self, device_id: str, app_path: str) -> bool:
        """
        Método responsável por instalar um app no dispositivo.

        Args:
            device_id (str): ID do dispositivo.
            app_path (str): Caminho do app.

        Returns:
            bool: True se instalar, False se não instalar.
        """
        cmd = (
            f'{self.adb_executable_path} -s {device_id} install -r {app_path}'
        )
        result = os.popen(cmd).readlines()
        if 'Success' in result[1]:
            return True
        else:
            return False
