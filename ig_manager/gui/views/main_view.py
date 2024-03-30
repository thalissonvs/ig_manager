from PyQt5.QtWidgets import QMainWindow

from ig_manager.guirc.main_view_rc import GUIKwaiBot


class MainView(QMainWindow, GUIKwaiBot):
    def __init__(self) -> None:
        super(MainView, self).__init__()
        self.setupUi(self)
