from PyQt5.QtWidgets import QMainWindow

from src.gui.views.main_view import GUIKwaiBot


class MainView(QMainWindow, GUIKwaiBot):
    def __init__(self) -> None:
        super(MainView, self).__init__()
        self.setupUi(self)
