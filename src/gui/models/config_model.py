from PyQt5.QtCore import QObject, pyqtSignal


class ConfigModel(QObject):

    time_between_actions_min_changed = pyqtSignal(int)
    time_between_actions_max_changed = pyqtSignal(int)
    actions_to_switch_account_changed = pyqtSignal(int)
    switch_account_with_no_tasks_changed = pyqtSignal(int)
    time_without_tasks_to_wait_changed = pyqtSignal(int)
    perform_like_actions_changed = pyqtSignal(bool)
    perform_follow_actions_changed = pyqtSignal(bool)
    enable_goal_changed = pyqtSignal(bool)
    actions_goal_changed = pyqtSignal(int)
    enable_rest_goal_changed = pyqtSignal(bool)
    rest_goal_actions_changed = pyqtSignal(int)
    rest_goal_time_changed = pyqtSignal(int)

    def __init__(self) -> None:
        super().__init__()
        self._time_between_actions_min = 0
        self._time_between_actions_max = 0
        self._actions_to_switch_account = 0
        self._switch_account_with_no_tasks = 0
        self._time_without_tasks_to_wait = 0
        self._perform_like_actions = False
        self._perform_follow_actions = False
        self._enable_goal = False
        self._actions_goal = 0
        self._enable_rest_goal = False
        self._rest_goal_actions = 0
        self._rest_goal_time = 0

    @property
    def time_between_actions_min(self) -> int:
        return self._time_between_actions_min

    @time_between_actions_min.setter
    def time_between_actions_min(self, value: int) -> None:
        self._time_between_actions_min = value
        self.time_between_actions_min_changed.emit(value)

    @property
    def time_between_actions_max(self) -> int:
        return self._time_between_actions_max

    @time_between_actions_max.setter
    def time_between_actions_max(self, value: int) -> None:
        self._time_between_actions_max = value
        self.time_between_actions_max_changed.emit(value)

    @property
    def actions_to_switch_account(self) -> int:
        return self._actions_to_switch_account

    @actions_to_switch_account.setter
    def actions_to_switch_account(self, value: int) -> None:
        self._actions_to_switch_account = value
        self.actions_to_switch_account_changed.emit(value)

    @property
    def switch_account_with_no_tasks(self) -> int:
        return self._switch_account_with_no_tasks

    @switch_account_with_no_tasks.setter
    def switch_account_with_no_tasks(self, value: int) -> None:
        self._switch_account_with_no_tasks = value
        self.switch_account_with_no_tasks_changed.emit(value)

    @property
    def time_without_tasks_to_wait(self) -> int:
        return self._time_without_tasks_to_wait

    @time_without_tasks_to_wait.setter
    def time_without_tasks_to_wait(self, value: int) -> None:
        self._time_without_tasks_to_wait = value
        self.time_without_tasks_to_wait_changed.emit(value)

    @property
    def perform_like_actions(self) -> bool:
        return self._perform_like_actions

    @perform_like_actions.setter
    def perform_like_actions(self, value: bool) -> None:
        self._perform_like_actions = value
        self.perform_like_actions_changed.emit(value)

    @property
    def perform_follow_actions(self) -> bool:
        return self._perform_follow_actions

    @perform_follow_actions.setter
    def perform_follow_actions(self, value: bool) -> None:
        self._perform_follow_actions = value
        self.perform_follow_actions_changed.emit(value)

    @property
    def enable_goal(self) -> bool:
        return self._enable_goal

    @enable_goal.setter
    def enable_goal(self, value: bool) -> None:
        self._enable_goal = value
        self.enable_goal_changed.emit(value)

    @property
    def actions_goal(self) -> int:
        return self._actions_goal

    @actions_goal.setter
    def actions_goal(self, value: int) -> None:
        self._actions_goal = value
        self.actions_goal_changed.emit(value)

    @property
    def enable_rest_goal(self) -> bool:
        return self._enable_rest_goal

    @enable_rest_goal.setter
    def enable_rest_goal(self, value: bool) -> None:
        self._enable_rest_goal = value
        self.enable_rest_goal_changed.emit(value)

    @property
    def rest_goal_actions(self) -> int:
        return self._rest_goal_actions

    @rest_goal_actions.setter
    def rest_goal_actions(self, value: int) -> None:
        self._rest_goal_actions = value
        self.rest_goal_actions_changed.emit(value)

    @property
    def rest_goal_time(self) -> int:
        return self._rest_goal_time

    @rest_goal_time.setter
    def rest_goal_time(self, value: int) -> None:
        self._rest_goal_time = value
        self.rest_goal_time_changed.emit(value)
