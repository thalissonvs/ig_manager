class OptionsKeys:
    TIME_BETWEEN_ACTIONS_MIN = 'time_between_actions_min'
    TIME_BETWEEN_ACTIONS_MAX = 'time_between_actions_max'
    ACTIONS_TO_SWITCH_ACCOUNT = 'actions_to_switch_account'
    SWITCH_ACCOUNT_WITH_NO_TASKS = 'switch_account_with_no_tasks'
    TIME_WITHOUT_TASKS_TO_WAIT = 'time_without_tasks_to_wait'
    PERFORM_LIKE_ACTIONS = 'perform_like_actions'
    PERFORM_FOLLOW_ACTIONS = 'perform_follow_actions'
    ENABLE_GOAL = 'enable_goal'
    ACTIONS_GOAL = 'actions_goal'
    ENABLE_REST_GOAL = 'enable_rest_goal'
    REST_GOAL_ACTIONS = 'rest_goal_actions'
    REST_GOAL_TIME = 'rest_goal_time'


DEFAULT_OPTIONS = {
    OptionsKeys.TIME_BETWEEN_ACTIONS_MIN: 5,
    OptionsKeys.TIME_BETWEEN_ACTIONS_MAX: 10,
    OptionsKeys.ACTIONS_TO_SWITCH_ACCOUNT: 50,
    OptionsKeys.SWITCH_ACCOUNT_WITH_NO_TASKS: True,
    OptionsKeys.TIME_WITHOUT_TASKS_TO_WAIT: 30,
    OptionsKeys.PERFORM_LIKE_ACTIONS: True,
    OptionsKeys.PERFORM_FOLLOW_ACTIONS: True,
    OptionsKeys.ENABLE_GOAL: True,
    OptionsKeys.ACTIONS_GOAL: 200,
    OptionsKeys.ENABLE_REST_GOAL: True,
    OptionsKeys.REST_GOAL_ACTIONS: 25,
    OptionsKeys.REST_GOAL_TIME: 60,
}
