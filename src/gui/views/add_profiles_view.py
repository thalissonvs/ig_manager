from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.gui.resources.add_profiles_view_rc import AddProfilesGUI
from src.gui.controllers.profiles_controller import ProfilesController


class AddProfilesView(AddProfilesGUI, QMainWindow):
    def __init__(self, profiles_controller: ProfilesController, parent=None) -> None:
        super(AddProfilesView, self).__init__(parent)
        self.setupUi(self)
        self._profiles_controller = profiles_controller
        self.setFixedSize(440, 280)
        self.button_add_profiles.clicked.connect(self._add_profiles)
        self.radiobutton_change_actions.toggled.connect(self.change_gui_widgets)
        self.radiobutton_change_actions.setChecked(True)

    def change_gui_widgets(self) -> None:
        if self.radiobutton_change_actions.isChecked():
            self.frame_profiles.hide()
            self.frame_username.show()
            self.frame_password.show()
            self.frame_gender.show()
        else:
            self.frame_profiles.show()
            self.frame_username.hide()
            self.frame_password.hide()
            self.frame_gender.hide()

    def _get_profile_info(self) -> dict:
        return {
            'username': self.lineedit_username.text(),
            'password': self.lineedit_password.text(),
            'gender': 'M' if self.combobox_gender.currentIndex() == 0 else 'F',
        }
    
    def _get_multiples_profiles_text(self) -> str:
        return self.textedit_profiles.toPlainText()
    
    def _add_profiles(self) -> None:
        if self.radiobutton_change_actions.isChecked():
            self._add_single_profile()
        else:
            self._add_multiple_profiles()
        
        self.close()
    
    def _add_single_profile(self) -> None:
        profile_info = self._get_profile_info()
        self._profiles_controller.add_single_profile(
            **profile_info
        )
    
    def _add_multiple_profiles(self) -> None:
        profiles_text = self._get_multiples_profiles_text()
        self._profiles_controller.add_multiple_profiles(profiles_text)
        
    

