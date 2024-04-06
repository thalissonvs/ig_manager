import json
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from PyQt5.QtWidgets import QApplication

from src.gui.constants import OptionsKeys
from src.gui.controllers.config_controller import ConfigController
from src.gui.models.config_model import ConfigModel
from src.gui.views.main_view import MainView


class TestGUIIntegration(TestCase):
    """
    Classe responsável por testar a integração da view MainView com suas dependências.
    """

    def setUp(self) -> None:
        self.app = QApplication(sys.argv)
        self.config_model = ConfigModel()
        self.config_controller = ConfigController(self.config_model)
        self.main_view = MainView(self.config_model, self.config_controller)

    def test_click_button_save_config_should_call_save_options(self) -> None:
        self.config_controller.save_options = MagicMock()
        self.main_view.button_save_config.click()
        self.config_controller.save_options.assert_called_once()

    def test_set_config_model_value_should_update_view(self) -> None:
        self.config_model.time_between_actions_min = 10
        self.config_model.time_between_actions_max = 20
        self.config_model.actions_to_switch_account = 30
        self.config_model.switch_account_with_no_tasks = False
        self.config_model.time_without_tasks_to_wait = 40
        self.config_model.perform_like_actions = False
        self.config_model.perform_follow_actions = False
        self.config_model.enable_goal = False
        self.config_model.actions_goal = 50
        self.config_model.enable_rest_goal = False
        self.config_model.rest_goal_actions = 60
        self.config_model.rest_goal_time = 70

        self.assertEqual(
            self.main_view.get_time_between_actions_min_value(), 10
        )
        self.assertEqual(
            self.main_view.get_time_between_actions_max_value(), 20
        )
        self.assertEqual(
            self.main_view.get_actions_to_switch_account_value(), 30
        )
        self.assertEqual(
            self.main_view.get_switch_account_with_no_tasks_value(), False
        )
        self.assertEqual(
            self.main_view.get_time_without_tasks_to_wait_value(), 40
        )
        self.assertEqual(
            self.main_view.get_perform_like_actions_value(), False
        )
        self.assertEqual(
            self.main_view.get_perform_follow_actions_value(), False
        )
        self.assertEqual(self.main_view.get_enable_goal_value(), False)
        self.assertEqual(self.main_view.get_actions_goal_value(), 50)
        self.assertEqual(self.main_view.get_enable_rest_goal_value(), False)
        self.assertEqual(self.main_view.get_rest_goal_actions_value(), 60)
        self.assertEqual(self.main_view.get_rest_goal_time_value(), 70)

    def test_config_controller_set_default_options_should_update_view(
        self,
    ) -> None:

        self.config_controller.set_default_options()

        self.assertEqual(
            self.main_view.get_time_between_actions_min_value(), 5
        )
        self.assertEqual(
            self.main_view.get_time_between_actions_max_value(), 10
        )
        self.assertEqual(
            self.main_view.get_actions_to_switch_account_value(), 50
        )
        self.assertEqual(
            self.main_view.get_switch_account_with_no_tasks_value(), True
        )
        self.assertEqual(
            self.main_view.get_time_without_tasks_to_wait_value(), 30
        )
        self.assertEqual(self.main_view.get_perform_like_actions_value(), True)
        self.assertEqual(
            self.main_view.get_perform_follow_actions_value(), True
        )
        self.assertEqual(self.main_view.get_enable_goal_value(), True)
        self.assertEqual(self.main_view.get_actions_goal_value(), 200)
        self.assertEqual(self.main_view.get_enable_rest_goal_value(), True)
        self.assertEqual(self.main_view.get_rest_goal_actions_value(), 25)
        self.assertEqual(self.main_view.get_rest_goal_time_value(), 60)

    def test_config_controller_load_options_with_valid_params_should_update_view(
        self,
    ) -> None:
        options = {
            OptionsKeys.TIME_BETWEEN_ACTIONS_MIN: 2,
            OptionsKeys.TIME_BETWEEN_ACTIONS_MAX: 5,
            OptionsKeys.ACTIONS_TO_SWITCH_ACCOUNT: 100,
            OptionsKeys.SWITCH_ACCOUNT_WITH_NO_TASKS: False,
            OptionsKeys.TIME_WITHOUT_TASKS_TO_WAIT: 60,
            OptionsKeys.PERFORM_LIKE_ACTIONS: False,
            OptionsKeys.PERFORM_FOLLOW_ACTIONS: False,
            OptionsKeys.ENABLE_GOAL: False,
            OptionsKeys.ACTIONS_GOAL: 150,
            OptionsKeys.ENABLE_REST_GOAL: False,
            OptionsKeys.REST_GOAL_ACTIONS: 20,
            OptionsKeys.REST_GOAL_TIME: 30,
        }
        self.config_controller.load_options(options)

        self.assertEqual(
            self.main_view.get_time_between_actions_min_value(), 2
        )
        self.assertEqual(
            self.main_view.get_time_between_actions_max_value(), 5
        )
        self.assertEqual(
            self.main_view.get_actions_to_switch_account_value(), 100
        )
        self.assertEqual(
            self.main_view.get_switch_account_with_no_tasks_value(), False
        )
        self.assertEqual(
            self.main_view.get_time_without_tasks_to_wait_value(), 60
        )
        self.assertEqual(
            self.main_view.get_perform_like_actions_value(), False
        )
        self.assertEqual(
            self.main_view.get_perform_follow_actions_value(), False
        )
        self.assertEqual(self.main_view.get_enable_goal_value(), False)
        self.assertEqual(self.main_view.get_actions_goal_value(), 150)
        self.assertEqual(self.main_view.get_enable_rest_goal_value(), False)
        self.assertEqual(self.main_view.get_rest_goal_actions_value(), 20)
        self.assertEqual(self.main_view.get_rest_goal_time_value(), 30)

    def test_config_controller_save_options_should_update_view(self):
        options = {
            OptionsKeys.TIME_BETWEEN_ACTIONS_MIN: 2,
            OptionsKeys.TIME_BETWEEN_ACTIONS_MAX: 5,
            OptionsKeys.ACTIONS_TO_SWITCH_ACCOUNT: 100,
            OptionsKeys.SWITCH_ACCOUNT_WITH_NO_TASKS: False,
            OptionsKeys.TIME_WITHOUT_TASKS_TO_WAIT: 60,
            OptionsKeys.PERFORM_LIKE_ACTIONS: False,
            OptionsKeys.PERFORM_FOLLOW_ACTIONS: False,
            OptionsKeys.ENABLE_GOAL: False,
            OptionsKeys.ACTIONS_GOAL: 150,
            OptionsKeys.ENABLE_REST_GOAL: False,
            OptionsKeys.REST_GOAL_ACTIONS: 20,
            OptionsKeys.REST_GOAL_TIME: 30,
        }

        self.config_controller.show_popup_signal = MagicMock()

        with patch('builtins.open', create=True) as mock_open:
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            self.config_controller.save_options(options)

            self.assertEqual(
                self.main_view.get_time_between_actions_min_value(), 2
            )
            self.assertEqual(
                self.main_view.get_time_between_actions_max_value(), 5
            )
            self.assertEqual(
                self.main_view.get_actions_to_switch_account_value(), 100
            )
            self.assertEqual(
                self.main_view.get_switch_account_with_no_tasks_value(), False
            )
            self.assertEqual(
                self.main_view.get_time_without_tasks_to_wait_value(), 60
            )
            self.assertEqual(
                self.main_view.get_perform_like_actions_value(), False
            )
            self.assertEqual(
                self.main_view.get_perform_follow_actions_value(), False
            )
            self.assertEqual(self.main_view.get_enable_goal_value(), False)
            self.assertEqual(self.main_view.get_actions_goal_value(), 150)
            self.assertEqual(
                self.main_view.get_enable_rest_goal_value(), False
            )
            self.assertEqual(self.main_view.get_rest_goal_actions_value(), 20)
            self.assertEqual(self.main_view.get_rest_goal_time_value(), 30)
