from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.gui.controllers.groups_controller import GroupsController
from src.gui.resources.add_profiles_view_rc import AddProfilesGUI


class AddProfilesView(AddProfilesGUI, QMainWindow):
    def __init__(
        self, groups_controller: GroupsController, parent=None
    ) -> None:
        super(AddProfilesView, self).__init__(parent)
        self.setupUi(self)
        self._groups_controller = groups_controller
        self.button_add_profiles.clicked.connect(self._add_profiles)
        self.radiobutton_single_profile.setChecked(True)
        self.radiobutton_single_profile.toggled.connect(self._toggle_gui)
        self.combobox_gender.currentIndexChanged.connect(self._toggle_gui)
        self.combobox_groups.currentIndexChanged.connect(self._toggle_gui)
        self._groups_controller.group_added.connect(
            self.add_groups_to_combobox
        )
        self._toggle_gui()
        self.add_groups_to_combobox()

    def add_groups_to_combobox(self) -> None:
        self.reset_combobox_groups()
        groups = self._groups_controller.get_groups()
        option = 'Criar novo grupo'
        for group in groups:
            option = f"{group['index']} - {group['group_name']}"
            self.combobox_groups.addItem(option)
        self.combobox_groups.setCurrentText(option)

    def reset_combobox_groups(self) -> None:
        self.combobox_groups.clear()
        self.combobox_groups.addItem('Criar novo grupo')
        self.combobox_groups.setCurrentText('Criar novo grupo')

    def _toggle_gui(self) -> None:
        if self.combobox_groups.currentIndex() == 0:
            self.frame_group_name.show()
            self.frame_device_id.show()
        else:
            self.frame_group_name.hide()
            self.frame_device_id.hide()

        if self.radiobutton_single_profile.isChecked():
            self.frame_username.show()
            self.frame_password.show()
            self.frame_gender.show()
            self.frame_profiles.hide()
        else:
            self.frame_username.hide()
            self.frame_password.hide()
            self.frame_gender.hide()
            self.frame_profiles.show()

    def _get_profile_info(self) -> dict:
        return {
            'username': self.lineedit_username.text(),
            'password': self.lineedit_password.text(),
            'gender': 'M' if self.combobox_gender.currentIndex() == 0 else 'F',
        }

    def _get_multiples_profiles_text(self) -> str:
        return self.textedit_profiles.toPlainText()

    def _add_profiles(self) -> None:
        if self.radiobutton_single_profile.isChecked():
            self._add_single_profile()
        else:
            self._add_multiple_profiles()

        self.close()

    def _add_single_profile(self) -> None:
        self._create_group_if_selected()
        group_index = int(self.combobox_groups.currentText().split(' - ')[0])
        profile_info = self._get_profile_info()
        self._groups_controller.add_profile_to_group(
            group_index,
            profile_info['username'],
            profile_info['password'],
            profile_info['gender'],
        )

    def _add_multiple_profiles(self) -> None:
        self._create_group_if_selected()
        group_index = int(self.combobox_groups.currentText().split(' - ')[0])
        profiles_text = self._get_multiples_profiles_text()
        self._groups_controller.add_multiples_profiles_to_group(
            group_index, profiles_text
        )

    def _create_group_if_selected(self) -> None:
        if self.combobox_groups.currentIndex() == 0:
            group_name = self.lineedit_group_name.text()
            device_id = self.lineedit_device_id.text()
            self._groups_controller.create_group(group_name, device_id)
            self.add_groups_to_combobox()
