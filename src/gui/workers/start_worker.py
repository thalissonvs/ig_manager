import time

from PyQt5 import QtCore

from src.gui.controllers.start_controller import StartController


class StartWorker(QtCore.QThread):

    finished = QtCore.pyqtSignal()

    def __init__(self, start_controller: StartController) -> None:
        super().__init__()
        self.start_controller = start_controller
        self.group_index = None

    def run(self) -> None:
        while self.group_index is None:
            time.sleep(1)
        self.start_controller.start_bot(self.group_index)
