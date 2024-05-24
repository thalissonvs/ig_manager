from PyQt5.QtWidgets import QMainWindow

from src.gui.controllers.groups_controller import GroupsController
from src.gui.resources.edit_profile_view_rc import EditProfileGUI


class EditProfileView(EditProfileGUI, QMainWindow):
    def __init__(
        self, groups_controller: GroupsController, parent=None
    ) -> None:
        super(EditProfileView, self).__init__(parent)
        self.setupUi(self)
        self._groups_controller = groups_controller
        self._old_username = None
        self._group_index = None
        self.button_save.clicked.connect(self.save_profile)

    def setup_view(self, group_index: int, profile_info: dict) -> None:
        self._group_index = group_index
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
        self._groups_controller.edit_group_profile_data(
            self._group_index, self._old_username, username, password, gender
        )
        self.close()
