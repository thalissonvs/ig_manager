from unittest import TestCase
from unittest.mock import MagicMock

from src.gui.models.config_model import ConfigModel


class TestConfigModel(TestCase):
    def setUp(self):
        self.config_model = ConfigModel()

    def test_time_between_actions_min(self):
        value = 5
        self.config_model.time_between_actions_min = value
        self.assertEqual(self.config_model.time_between_actions_min, value)

    def test_time_between_actions_max(self):
        value = 10
        self.config_model.time_between_actions_max = value
        self.assertEqual(self.config_model.time_between_actions_max, value)

    def test_actions_to_switch_account(self):
        value = 100
        self.config_model.actions_to_switch_account = value
        self.assertEqual(self.config_model.actions_to_switch_account, value)

    def test_switch_account_with_no_tasks(self):
        value = 0
        self.config_model.switch_account_with_no_tasks = value
        self.assertEqual(self.config_model.switch_account_with_no_tasks, value)

    def test_time_without_tasks_to_wait(self):
        value = 60
        self.config_model.time_without_tasks_to_wait = value
        self.assertEqual(self.config_model.time_without_tasks_to_wait, value)

    def test_perform_like_actions(self):
        value = True
        self.config_model.perform_like_actions = value
        self.assertEqual(self.config_model.perform_like_actions, value)

    def test_perform_follow_actions(self):
        value = False
        self.config_model.perform_follow_actions = value
        self.assertEqual(self.config_model.perform_follow_actions, value)

    def test_enable_goal(self):
        value = True
        self.config_model.enable_goal = value
        self.assertEqual(self.config_model.enable_goal, value)

    def test_actions_goal(self):
        value = 150
        self.config_model.actions_goal = value
        self.assertEqual(self.config_model.actions_goal, value)

    def test_enable_rest_goal(self):
        value = False
        self.config_model.enable_rest_goal = value
        self.assertEqual(self.config_model.enable_rest_goal, value)

    def test_rest_goal_actions(self):
        value = 20
        self.config_model.rest_goal_actions = value
        self.assertEqual(self.config_model.rest_goal_actions, value)

    def test_rest_goal_time(self):
        value = 30
        self.config_model.rest_goal_time = value
        self.assertEqual(self.config_model.rest_goal_time, value)
