import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.gui.constants import OptionsKeys
from src.gui.controllers.config_controller import ConfigController
from src.gui.controllers.devices_controller import DevicesController
from src.gui.controllers.groups_controller import GroupsController
from src.gui.controllers.start_controller import StartController
from src.gui.resources.main_view_rc import IGBotGUI
from src.gui.views.add_profiles_view import AddProfilesView
from src.gui.views.edit_profile_view import EditProfileView
from src.gui.views.group_view import GroupView


class MainView(IGBotGUI, QMainWindow):
    def __init__(
        self,
        config_controller: ConfigController,
        devices_controller: DevicesController,
        groups_controller: GroupsController,
        start_controller: StartController,
        add_profiles_view: AddProfilesView,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.config_controller = config_controller
        self.devices_controller = devices_controller
        self.groups_controller = groups_controller
        self.start_controller = start_controller
        self.add_profiles_view = add_profiles_view
        self.group_views: dict[int, GroupView] = {}

        self.config_controller.config_changed.connect(self.set_options_at_view)
        self.config_controller.set_initial_options()

        self.devices_controller.device_added.connect(self.set_device_on_view)
        self.devices_controller.device_removed.connect(
            self.remove_device_from_view
        )
        self.devices_controller.show_popup_signal.connect(self.show_popup)
        self.devices_controller.watch_devices()

        self.groups_controller.group_added.connect(self.create_group_frame)
        self.groups_controller.group_removed.connect(self.remove_group_frame)
        self.groups_controller.group_edited.connect(self.edit_group_frame)

        self.groups_controller.show_popup_signal.connect(self.show_popup)
        self.groups_controller.set_repository_to_model()

        self.start_controller.show_popup_signal.connect(self.show_popup)

        self.button_save_config.clicked.connect(self.save_options)
        self.button_change_to_wifi.clicked.connect(
            lambda: self.devices_controller.change_devices_connection_to_wifi(
                self.textedit_usb_devices.toPlainText()
            )
        )
        self.button_connect_emulators.clicked.connect(
            lambda: self.devices_controller.connect_devices_with_ip_address(
                self.textedit_connect_emulators.toPlainText()
            )
        )
        self.button_add_profiles.clicked.connect(self.add_profiles_view.show)

        self.set_page_events()
        self.set_widgets_events()
        self.frame_4.hide()
        self.frame_5.hide()   # temporário
        self.frame_33.hide()

    def set_page_events(self) -> None:
        self.page_devices.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2)
        )
        self.page_start.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )
        self.page_options.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )

    def set_widgets_events(self) -> None:
        self.radiobutton_change_actions.toggled.connect(
            self.update_widtgets_visibility
        )
        self.radiobutton_enable_goal.toggled.connect(
            self.update_widtgets_visibility
        )
        self.radiobutton_enable_rest_goal.toggled.connect(
            self.update_widtgets_visibility
        )

    def set_options_at_view(self, options: dict) -> None:
        self.set_time_between_actions_min_value(
            options[OptionsKeys.TIME_BETWEEN_ACTIONS_MIN]
        )
        self.set_time_between_actions_max_value(
            options[OptionsKeys.TIME_BETWEEN_ACTIONS_MAX]
        )
        self.set_actions_to_switch_account_value(
            options[OptionsKeys.ACTIONS_TO_SWITCH_ACCOUNT]
        )
        self.set_switch_account_with_no_tasks_value(
            options[OptionsKeys.SWITCH_ACCOUNT_WITH_NO_TASKS]
        )
        self.set_time_without_tasks_to_wait_value(
            options[OptionsKeys.TIME_WITHOUT_TASKS_TO_WAIT]
        )
        self.set_perform_like_actions_value(
            options[OptionsKeys.PERFORM_LIKE_ACTIONS]
        )
        self.set_perform_follow_actions_value(
            options[OptionsKeys.PERFORM_FOLLOW_ACTIONS]
        )
        self.set_enable_goal_value(options[OptionsKeys.ENABLE_GOAL])
        self.set_actions_goal_value(options[OptionsKeys.ACTIONS_GOAL])
        self.set_enable_rest_goal_value(options[OptionsKeys.ENABLE_REST_GOAL])
        self.set_rest_goal_actions_value(
            options[OptionsKeys.REST_GOAL_ACTIONS]
        )
        self.set_rest_goal_time_value(options[OptionsKeys.REST_GOAL_TIME])
        self.set_automation_app_value(options[OptionsKeys.AUTOMATION_APP])

    def save_options(self) -> None:
        options_object = self.get_options_object()
        self.config_controller.save_options(options_object)

    def update_widtgets_visibility(self) -> None:
        if self.radiobutton_change_actions.isChecked():
            self.frame_change_actions.show()
        else:
            self.frame_change_actions.hide()

        if self.radiobutton_enable_goal.isChecked():
            self.frame_goal_actions.show()
        else:
            self.frame_goal_actions.hide()

        if self.radiobutton_enable_rest_goal.isChecked():
            self.frame_rest_goal.show()
        else:
            self.frame_rest_goal.hide()

    def get_options_object(self) -> dict:
        return {
            OptionsKeys.TIME_BETWEEN_ACTIONS_MIN: self.get_time_between_actions_min_value(),
            OptionsKeys.TIME_BETWEEN_ACTIONS_MAX: self.get_time_between_actions_max_value(),
            OptionsKeys.ACTIONS_TO_SWITCH_ACCOUNT: self.get_actions_to_switch_account_value(),
            OptionsKeys.SWITCH_ACCOUNT_WITH_NO_TASKS: self.get_switch_account_with_no_tasks_value(),
            OptionsKeys.TIME_WITHOUT_TASKS_TO_WAIT: self.get_time_without_tasks_to_wait_value(),
            OptionsKeys.PERFORM_LIKE_ACTIONS: self.get_perform_like_actions_value(),
            OptionsKeys.PERFORM_FOLLOW_ACTIONS: self.get_perform_follow_actions_value(),
            OptionsKeys.ENABLE_GOAL: self.get_enable_goal_value(),
            OptionsKeys.ACTIONS_GOAL: self.get_actions_goal_value(),
            OptionsKeys.ENABLE_REST_GOAL: self.get_enable_rest_goal_value(),
            OptionsKeys.REST_GOAL_ACTIONS: self.get_rest_goal_actions_value(),
            OptionsKeys.REST_GOAL_TIME: self.get_rest_goal_time_value(),
            OptionsKeys.AUTOMATION_APP: self.get_automation_app_value(),
        }

    def show_popup(self, title: str, text: str) -> None:
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Information)
        msg.exec_()

    def set_time_between_actions_min_value(self, value: int) -> None:
        self.spinbox_min_time_actions.setValue(value)

    def set_time_between_actions_max_value(self, value: int) -> None:
        self.spinbox_max_time_actions.setValue(value)

    def set_actions_to_switch_account_value(self, value: int) -> None:
        self.spinbox_actions_change_amount.setValue(value)

    def set_switch_account_with_no_tasks_value(self, value: bool) -> None:
        self.radiobutton_change_actions.setChecked(value)
        self.radiobutton_dont_change_actions.setChecked(not value)

    def set_time_without_tasks_to_wait_value(self, value: int) -> None:
        self.spinbox_seconds_to_change.setValue(value)

    def set_perform_like_actions_value(self, value: bool) -> None:
        self.checkbox_like.setChecked(value)

    def set_perform_follow_actions_value(self, value: bool) -> None:
        self.checkbox_follow.setChecked(value)

    def set_enable_goal_value(self, value: bool) -> None:
        self.radiobutton_enable_goal.setChecked(value)
        self.radiobutton_disable_goal.setChecked(not value)

    def set_actions_goal_value(self, value: int) -> None:
        self.spinbox_goal_actions.setValue(value)

    def set_enable_rest_goal_value(self, value: bool) -> None:
        self.radiobutton_enable_rest_goal.setChecked(value)
        self.radiobutton_disable_rest_goal.setChecked(not value)

    def set_rest_goal_actions_value(self, value: int) -> None:
        self.spinbox_actions_rest.setValue(value)

    def set_rest_goal_time_value(self, value: int) -> None:
        self.spinbox_minutes_rest.setValue(value)

    def set_automation_app_value(self, value: str) -> None:
        self.radiobutton_lite_instagram.setChecked(value == 'lite_instagram')
        self.radiobutton_official_instagram.setChecked(
            value == 'official_instagram'
        )

    def get_time_between_actions_min_value(self) -> int:
        return self.spinbox_min_time_actions.value()

    def get_time_between_actions_max_value(self) -> int:
        return self.spinbox_max_time_actions.value()

    def get_actions_to_switch_account_value(self) -> int:
        return self.spinbox_actions_change_amount.value()

    def get_switch_account_with_no_tasks_value(self) -> bool:
        return self.radiobutton_change_actions.isChecked()

    def get_time_without_tasks_to_wait_value(self) -> int:
        return self.spinbox_seconds_to_change.value()

    def get_perform_like_actions_value(self) -> bool:
        return self.checkbox_like.isChecked()

    def get_perform_follow_actions_value(self) -> bool:
        return self.checkbox_follow.isChecked()

    def get_enable_goal_value(self) -> bool:
        return self.radiobutton_enable_goal.isChecked()

    def get_actions_goal_value(self) -> int:
        return self.spinbox_goal_actions.value()

    def get_enable_rest_goal_value(self) -> bool:
        return self.radiobutton_enable_rest_goal.isChecked()

    def get_rest_goal_actions_value(self) -> int:
        return self.spinbox_actions_rest.value()

    def get_rest_goal_time_value(self) -> int:
        return self.spinbox_minutes_rest.value()

    def get_automation_app_value(self) -> str:
        return (
            'lite_instagram'
            if self.radiobutton_lite_instagram.isChecked()
            else 'official_instagram'
        )

    def set_device_on_view(self, device_info: dict) -> None:
        self._create_device_frame(device_info)

        if device_info['connection_type'] == 'usb':
            self.textedit_usb_devices.appendPlainText(
                device_info['device_id'] + '\n'
            )

        if self._should_remove_no_devices_connected():
            self.combobox_connected_devices.removeItem(0)

        self.combobox_connected_devices.addItem(
            f"[ID] {device_info['device_id']} - [MODEL] {device_info['model']}"
        )

    def remove_device_from_view(self, device_info: dict) -> None:
        self._delete_device_frame(device_info['index'])
        if device_info['device_id'] in self.textedit_usb_devices.toPlainText():
            usb_devices = self.textedit_usb_devices.toPlainText()
            new_usb_devices = usb_devices.replace(
                device_info['device_id'] + '\n', ''
            )
            self.textedit_usb_devices.setPlainText(new_usb_devices)
        self.combobox_connected_devices.removeItem(
            self.combobox_connected_devices.findText(
                f"[ID] {device_info['device_id']} - [MODEL] {device_info['model']}"
            )
        )
        if self._should_add_no_devices_connected():
            self.combobox_connected_devices.addItem(
                'Nenhum dispositivo conectado'
            )

    def _should_remove_no_devices_connected(self) -> bool:
        combobox_devices_items = self._get_combobox_devices_items()
        return 'Nenhum dispositivo conectado' in combobox_devices_items

    def _should_add_no_devices_connected(self) -> bool:
        combobox_devices_items = self._get_combobox_devices_items()
        return len(combobox_devices_items) == 0

    def _get_combobox_devices_items(self) -> list:
        return [
            self.combobox_connected_devices.itemText(i)
            for i in range(self.combobox_connected_devices.count())
        ]

    def _create_device_frame(self, device_info: dict) -> None:

        device_index = device_info['index']
        device_id = device_info['device_id']

        main_frame = self._create_device_main_frame(device_index)
        horizontal_layout = self._create_device_horizontal_layout(
            main_frame, device_index
        )
        frame_device_model = self._create_frame_device_model(
            main_frame, device_index
        )
        vertical_layout = self._create_device_model_vertical_layout(
            frame_device_model, device_index
        )
        label_device_model = self._create_label_device_model(
            frame_device_model, device_index
        )

        vertical_layout.addWidget(label_device_model)
        horizontal_layout.addWidget(frame_device_model)

        frame_device_connection = self._create_frame_device_connection(
            main_frame, device_index
        )
        vertical_layout_2 = self._create_device_connection_vertical_layout(
            frame_device_connection, device_index
        )
        selected_stylesheet = self._get_connection_stylesheet(
            device_info['connection_type']
        )
        frame_device_connection_icon = (
            self._create_frame_device_connection_icon(
                frame_device_connection, device_index
            )
        )
        frame_device_connection_icon.setStyleSheet(selected_stylesheet)

        vertical_layout_2.addWidget(
            frame_device_connection_icon, 0, QtCore.Qt.AlignHCenter
        )
        horizontal_layout.addWidget(frame_device_connection)

        frame_device_actions = self._create_frame_device_actions(
            main_frame, device_index
        )
        vertical_layout_3 = self._create_device_actions_vertical_layout(
            frame_device_actions, device_index
        )

        button_device_actions = self._create_button_device_actions(
            frame_device_actions, device_index
        )
        self._set_button_device_actions_menu(button_device_actions, device_id)

        vertical_layout_3.addWidget(
            button_device_actions, 0, QtCore.Qt.AlignHCenter
        )
        horizontal_layout.addWidget(frame_device_actions)

        label_device_model.setText(device_info['model'])

        self.verticalLayout_8.addWidget(main_frame)

    def _create_device_main_frame(self, device_index: int) -> QtWidgets.QFrame:
        main_frame = QtWidgets.QFrame(self.frame_3)
        main_frame.setMinimumSize(QtCore.QSize(0, 40))
        main_frame.setStyleSheet('')
        main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        main_frame.setObjectName('frame_device_' + str(device_index))
        return main_frame

    def _create_device_horizontal_layout(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QHBoxLayout:
        horizontal_layout = QtWidgets.QHBoxLayout(parent)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        horizontal_layout.setObjectName(
            'horizontalLayout_' + str(device_index)
        )
        return horizontal_layout

    def _create_frame_device_model(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QFrame:
        frame_device_model = QtWidgets.QFrame(parent)
        frame_device_model.setStyleSheet('border: 0px;')
        frame_device_model.setFrameShape(QtWidgets.QFrame.NoFrame)
        frame_device_model.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_device_model.setObjectName(
            'frame_device_model_' + str(device_index)
        )
        return frame_device_model

    def _create_device_model_vertical_layout(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QVBoxLayout:
        vertical_layout = QtWidgets.QVBoxLayout(parent)
        vertical_layout.setObjectName('verticalLayout_' + str(device_index))
        return vertical_layout

    def _create_label_device_model(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QLabel:
        label_device_model = QtWidgets.QLabel(parent)
        label_device_model.setStyleSheet(
            'font: 8pt "Yu Gothic UI Semilight";\n'
            'color: rgb(230, 230, 230);\n'
            'font-weight:bold;'
        )
        label_device_model.setAlignment(QtCore.Qt.AlignCenter)
        label_device_model.setObjectName(
            'label_device_model_' + str(device_index)
        )
        return label_device_model

    def _create_frame_device_connection(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QFrame:
        frame_device_connection = QtWidgets.QFrame(parent)
        frame_device_connection.setMaximumSize(QtCore.QSize(99, 16777215))
        frame_device_connection.setStyleSheet('')
        frame_device_connection.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_device_connection.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_device_connection.setObjectName(
            'frame_device_connection_' + str(device_index)
        )
        return frame_device_connection

    def _create_device_connection_vertical_layout(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QVBoxLayout:
        vertical_layout = QtWidgets.QVBoxLayout(parent)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.setSpacing(0)
        vertical_layout.setObjectName('verticalLayout2_' + str(device_index))
        return vertical_layout

    def _create_frame_device_connection_icon(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QFrame:
        frame_device_connection_icon = QtWidgets.QFrame(parent)
        frame_device_connection_icon.setMinimumSize(QtCore.QSize(22, 22))
        frame_device_connection_icon.setMaximumSize(QtCore.QSize(22, 20))
        frame_device_connection_icon.setStyleSheet('')
        frame_device_connection_icon.setFrameShape(
            QtWidgets.QFrame.StyledPanel
        )
        frame_device_connection_icon.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_device_connection_icon.setObjectName(
            'frame_device_connection_icon_' + str(device_index)
        )
        return frame_device_connection_icon

    def _create_frame_device_actions(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QFrame:
        frame_device_actions = QtWidgets.QFrame(parent)
        frame_device_actions.setStyleSheet('border: 0px;')
        frame_device_actions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_device_actions.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_device_actions.setObjectName(
            'frame_device_actions_' + str(device_index)
        )
        return frame_device_actions

    def _create_device_actions_vertical_layout(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QVBoxLayout:
        vertical_layout = QtWidgets.QVBoxLayout(parent)
        vertical_layout.setContentsMargins(0, 0, 0, 0)
        vertical_layout.setSpacing(0)
        vertical_layout.setObjectName('verticalLayout3_' + str(device_index))
        return vertical_layout

    def _create_button_device_actions(
        self, parent: QtWidgets.QFrame, device_index: int
    ) -> QtWidgets.QPushButton:
        button_device_actions = QtWidgets.QPushButton(parent)
        button_device_actions.setMinimumSize(QtCore.QSize(18, 18))
        button_device_actions.setMaximumSize(QtCore.QSize(18, 16777215))
        button_device_actions.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        button_device_actions.setStyleSheet(
            'background-image: url(:/imagens/imagens/more_resized.png);'
        )
        button_device_actions.setText('')
        button_device_actions.setObjectName(
            'button_device_actions_' + str(device_index)
        )
        return button_device_actions

    def _set_button_device_actions_menu(
        self, button_device_actions: QtWidgets.QPushButton, device_id: int
    ) -> None:
        menu = QtWidgets.QMenu()
        menu.addAction('Ver informações')
        menu.addAction(
            'Desconectar dispositivo',
            lambda: self.devices_controller.disconnect_device(device_id),
        )
        button_device_actions.setMenu(menu)

    def _get_connection_stylesheet(self, connection: str) -> str:
        usb_connection_stylesheet = """QFrame{background-image: url(:/imagens/imagens/usb_resized.png);
                                    background-position:center;background-repeat: none;border-radius: 11px;
                                    }\nQFrame:hover{background-color: rgb(70, 70, 82);}"""
        wifi_connection_stylesheet = """QFrame{background-image: url(:/imagens/imagens/wi-fi-resized.png);
                                    background-position:center;background-repeat: none;border-radius: 11px;
                                    }\nQFrame:hover{background-color: rgb(70, 70, 82);}"""
        return (
            wifi_connection_stylesheet
            if connection == 'wifi'
            else usb_connection_stylesheet
        )

    def _delete_device_frame(self, device_index: int) -> None:
        frame_device = self.findChild(
            QtWidgets.QFrame, 'frame_device_' + str(device_index)
        )
        frame_device.setParent(None)
        frame_device.deleteLater()

    def create_group_frame(self, group_info: dict) -> None:

        group_index = group_info['index']

        frame_group = QtWidgets.QFrame(self.frame_32)
        frame_group.setMinimumSize(QtCore.QSize(0, 40))
        frame_group.setStyleSheet('')
        frame_group.setFrameShape(QtWidgets.QFrame.NoFrame)
        frame_group.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_group.setObjectName('frame_group_' + str(group_index))

        horizontal_layout = QtWidgets.QHBoxLayout(frame_group)
        horizontal_layout.setContentsMargins(0, 0, 0, 0)
        horizontal_layout.setSpacing(0)
        horizontal_layout.setObjectName('horizontalLayout_' + str(group_index))

        frame_group_name = QtWidgets.QFrame(frame_group)
        frame_group_name.setMaximumSize(QtCore.QSize(150, 16777215))
        frame_group_name.setStyleSheet('')
        frame_group_name.setFrameShape(QtWidgets.QFrame.NoFrame)
        frame_group_name.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_group_name.setObjectName('frame_group_name_' + str(group_index))

        vertical_layout = QtWidgets.QVBoxLayout(frame_group_name)
        vertical_layout.setObjectName('verticalLayout_' + str(group_index))

        label_group_name = QtWidgets.QLabel(frame_group_name)
        label_group_name.setStyleSheet(
            'font: 8pt "Yu Gothic UI Semilight";\n'
            'color: rgb(230, 230, 230);\n'
            'font-weight:bold;'
        )
        label_group_name.setAlignment(QtCore.Qt.AlignCenter)
        label_group_name.setObjectName('label_group_name_' + str(group_index))

        vertical_layout.addWidget(label_group_name)
        horizontal_layout.addWidget(frame_group_name)

        frame_group_device = QtWidgets.QFrame(frame_group)
        frame_group_device.setMinimumSize(QtCore.QSize(236, 0))
        frame_group_device.setMaximumSize(QtCore.QSize(236, 16777215))
        frame_group_device.setStyleSheet('')
        frame_group_device.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_group_device.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_group_device.setObjectName(
            'frame_group_device_' + str(group_index)
        )

        vertical_layout2 = QtWidgets.QVBoxLayout(frame_group_device)
        vertical_layout2.setObjectName('verticalLayout2_' + str(group_index))

        label_group_device = QtWidgets.QLabel(frame_group_device)
        label_group_device.setStyleSheet(
            'font: 8pt "Yu Gothic UI Semilight";\n'
            'color: rgb(230, 230, 230);\n'
            'font-weight:bold;'
        )
        label_group_device.setAlignment(QtCore.Qt.AlignCenter)
        label_group_device.setObjectName(
            'label_group_device_' + str(group_index)
        )

        vertical_layout2.addWidget(label_group_device)
        horizontal_layout.addWidget(frame_group_device)

        frame_group_actions = QtWidgets.QFrame(frame_group)
        frame_group_actions.setMinimumSize(QtCore.QSize(20, 0))
        frame_group_actions.setStyleSheet('border: 0px;')
        frame_group_actions.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame_group_actions.setFrameShadow(QtWidgets.QFrame.Raised)
        frame_group_actions.setObjectName(
            'frame_group_actions_' + str(group_index)
        )

        vertical_layout3 = QtWidgets.QVBoxLayout(frame_group_actions)
        vertical_layout3.setContentsMargins(0, 0, 0, 0)
        vertical_layout3.setSpacing(0)
        vertical_layout3.setObjectName('verticalLayout3_' + str(group_index))

        button_open_group = QtWidgets.QPushButton(frame_group_actions)
        button_open_group.setMinimumSize(QtCore.QSize(20, 20))
        button_open_group.setMaximumSize(QtCore.QSize(20, 16777215))
        button_open_group.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor)
        )
        button_open_group.setStyleSheet(
            'background-image: url(:/imagens/imagens/eye-resized.png);'
        )
        button_open_group.setText('')
        button_open_group.setObjectName(
            'button_open_group_' + str(group_index)
        )
        button_open_group.clicked.connect(lambda: self.open_group(group_index))

        vertical_layout3.addWidget(
            button_open_group, 0, QtCore.Qt.AlignHCenter
        )
        horizontal_layout.addWidget(frame_group_actions)

        label_group_name.setText(group_info['group_name'])
        label_group_device.setText(group_info['device_id'])

        self.verticalLayout_26.addWidget(frame_group)

    def remove_group_frame(self, group_index: int) -> None:
        frame_group = self.findChild(
            QtWidgets.QFrame, 'frame_group_' + str(group_index)
        )
        frame_group.setParent(None)
        frame_group.deleteLater()

    def edit_group_frame(self, group_info: dict) -> None:
        group_index = group_info['index']
        label_group_name = self.findChild(
            QtWidgets.QLabel, 'label_group_name_' + str(group_index)
        )
        label_group_device = self.findChild(
            QtWidgets.QLabel, 'label_group_device_' + str(group_index)
        )
        label_group_name.setText(group_info['group_name'])
        label_group_device.setText(group_info['device_id'])

    def open_group(self, group_index: int) -> None:

        if group_index in self.group_views.keys():
            self.group_views[group_index].show()
            return

        edit_profile_view = EditProfileView(self.groups_controller)
        group = GroupView(
            edit_profile_view,
            self.groups_controller,
            self.start_controller,
            group_index,
        )
        self.group_views[group_index] = group
        group.show()
