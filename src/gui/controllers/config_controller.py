import json
import os

from PyQt5.QtCore import QObject

from src.gui.models.config_model import ConfigModel


class ConfigController(QObject):

    DEFAULT_OPTIONS = {
        'time_between_actions_min': 5,
        'time_between_actions_max': 10,
        'actions_to_switch_account': 50,
        'switch_account_with_no_tasks': True,
        'time_without_tasks_to_wait': 30,
        'perform_like_actions': True,
        'perform_follow_actions': True,
        'enable_goal': True,
        'actions_goal': 200,
        'enable_rest_goal': True,
        'rest_goal_actions': 25,
        'rest_goal_time': 60,
    }

    OPTIONS_PATH = os.path.join(os.getcwd(), 'userdata', 'options.json')

    def __init__(self, config_model: ConfigModel) -> None:
        super().__init__()
        self.config_model = config_model

    def set_default_options(self) -> None:
        for key, value in self.DEFAULT_OPTIONS.items():
            setattr(self.config_model, key, value)

    def set_options_if_valid(self) -> None:
        options_content = (
            open(self.OPTIONS_PATH, 'r').read()
            if os.path.exists(self.OPTIONS_PATH)
            else ''
        )

        try:
            options = json.loads(options_content)
        except json.JSONDecodeError:
            self.set_default_options()
            return

        self.load_options(options)

    def load_options(self, options: dict) -> None:
        for key, value in options.items():
            if key in self.DEFAULT_OPTIONS:
                setattr(self.config_model, key, value)

    def save_options(self, options: dict) -> None:
        for key, value in options.items():
            if key in self.DEFAULT_OPTIONS:
                setattr(self.config_model, key, value)

        with open(self.OPTIONS_PATH, 'w') as f:
            f.write(json.dumps(options, ident=4))
