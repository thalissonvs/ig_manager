from PyQt5.QtWidgets import QMainWindow

from src.gui.resources.main_view_rc import IGBotGUI


class MainView(IGBotGUI, QMainWindow):
    def __init__(self, config_model, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.config_model = config_model
        self.connect_config_model_signals()

    def connect_config_model_signals(self) -> None:
        self.config_model.time_between_actions_min_changed.connect(
            self.set_time_between_actions_min_value)
        self.config_model.time_between_actions_max_changed.connect(
            self.set_time_between_actions_max_value)
        self.config_model.actions_to_switch_account_changed.connect(
            self.set_actions_to_switch_account_value)
        self.config_model.switch_account_with_no_tasks_changed.connect(
            self.set_switch_account_with_no_tasks_value)
        self.config_model.time_without_tasks_to_wait_changed.connect(
            self.set_time_without_tasks_to_wait_value)
        self.config_model.perform_like_actions_changed.connect(
            self.set_perform_like_actions_value)
        self.config_model.perform_follow_actions_changed.connect(
            self.set_perform_follow_actions_value)
        self.config_model.enable_goal_changed.connect(
            self.set_enable_goal_value)
        self.config_model.actions_goal_changed.connect(
            self.set_actions_goal_value)
        self.config_model.enable_rest_goal_changed.connect(
            self.set_enable_rest_goal_value)
        self.config_model.rest_goal_actions_changed.connect(
            self.set_rest_goal_actions_value)
        self.config_model.rest_goal_time_changed.connect(
            self.set_rest_goal_time_value)

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
