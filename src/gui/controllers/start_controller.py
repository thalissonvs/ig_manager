from PyQt5.QtCore import QObject, pyqtSignal

from src.bot.start_facade import StartBotFacade
from src.gui.models.config_model import ConfigModel
from src.gui.models.devices_model import DevicesModel
from src.gui.models.groups_model import GroupsModel


class StartController(QObject):

    show_popup_signal = pyqtSignal(str, str)

    def __init__(
        self,
        devices_model: DevicesModel,
        groups_model: GroupsModel,
        config_model: ConfigModel,
        bot_facade: StartBotFacade,
    ) -> None:
        super().__init__()
        self._devices_model = devices_model
        self._groups_model = groups_model
        self._config_model = config_model
        self._bot_facade = bot_facade

    def start_bot(self, profile_info: dict, device_id: str = None) -> None:
        automation_platform = self._config_model.automation_platform

        if automation_platform == 'android' and not device_id:
            self.show_popup_signal.emit(
                'Erro',
                'Selecione um dispositivo para iniciar a automação.',
            )
            return

        try:
            self._bot_facade.start(
                self._devices_model,
                self._groups_model,
                self._config_model,
                profile_info,
                device_id,
            )
        except Exception as e:
            self.show_popup_signal.emit(
                'Erro',
                f'Erro ao iniciar o bot: {str(e)}',
            )
