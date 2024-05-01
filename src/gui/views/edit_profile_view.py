from PyQt5.QtWidgets import QMainWindow

from src.gui.controllers.profiles_controller import ProfilesController
from src.gui.resources.edit_profile_view_rc import EditProfileGUI


class EditProfileView(EditProfileGUI, QMainWindow):
    def __init__(
        self, profiles_controller: ProfilesController, parent=None
    ) -> None:
        super(EditProfileView, self).__init__(parent)
        self.setupUi(self)
        self._profiles_controller = profiles_controller
        self._old_username = None
        self.button_save.clicked.connect(self.save_profile)

    def setup_view(self, profile_info: dict) -> None:
        self._old_username = profile_info['username']
        self.lineedit_username.setText(self._old_username)
        self.lineedit_password.setText(profile_info['password'])
        self.combobox_gender.setCurrentText(
            'Masculino' if profile_info['gender'] == 'M' else 'Feminino'
        )
        self.show()

    def save_profile(self) -> None:
        username = self.lineedit_username.text()
        password = self.lineedit_password.text()
        gender = (
            'M' if self.combobox_gender.currentText() == 'Masculino' else 'F'
        )
        self._profiles_controller.edit_profile(
            self._old_username, username, password, gender
        )
        self.close()
