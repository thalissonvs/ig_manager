from PyQt5.QtWidgets import QMainWindow, QMessageBox

from src.gui.constants import OptionsKeys
from src.gui.controllers.config_controller import ConfigController
from src.gui.models.config_model import ConfigModel
from src.gui.resources.main_view_rc import IGBotGUI


class MainView(IGBotGUI, QMainWindow):
    def __init__(
        self,
        config_model: ConfigModel,
        config_controller: ConfigController,
        parent=None,
    ) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.config_model = config_model
        self.config_controller = config_controller
        self.config_controller.config_changed.connect(self.set_options_at_view)
        self.config_controller.set_initial_options()
        self.stackedWidget.setCurrentIndex(0)
        self.button_save_config.clicked.connect(self.save_options)

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

    def save_options(self) -> None:
        options_object = self.get_options_object()
        self.config_controller.save_options(options_object)

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
        }

    def show_popup(self, message: str, text: str) -> None:
        msg = QMessageBox()
        msg.setWindowTitle(message)
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
