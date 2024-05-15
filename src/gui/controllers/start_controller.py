from PyQt5.QtCore import QObject, pyqtSignal

from src.bot.start_facade import StartBotFacade
from src.gui.models.config_model import ConfigModel
from src.gui.models.devices_model import DevicesModel
from src.gui.models.groups_model import GroupsModel


class StartController(QObject):

    show_popup_signal = pyqtSignal(str, str)

    def __init__(
        self,
        bot_facade: StartBotFacade,
    ) -> None:
        super().__init__()
        self._bot_facade = bot_facade

    def start_bot(self, group_index: int) -> None:

        try:
            self._bot_facade.start(group_index)
        except Exception as e:
            self.show_popup_signal.emit(
                'Erro',
                f'Erro ao iniciar o bot: {str(e)}',
            )
