from ig_manager.guirc.main_view_rc import GUIKwaiBot
from PyQt5.QtWidgets import QMainWindow


class MainView(QMainWindow, GUIKwaiBot):
    def __init__(self, controller, config_model) -> None:
        super(MainView, self).__init__()
        self.setupUi(self)
        self.controller = controller
        self.config_model = config_model
