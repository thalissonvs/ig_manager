import json
import os
from unittest import TestCase
from unittest.mock import MagicMock, patch

from src.gui.constants import DEFAULT_OPTIONS, OptionsKeys
from src.gui.controllers.config_controller import ConfigController


class TestConfigController(TestCase):
    def setUp(self):
        self.config_model = MagicMock()
        self.config_controller = ConfigController(self.config_model)

    def test_set_default_options_should_update_model_properties(self):
        self.config_controller.set_default_options()
        for key, value in DEFAULT_OPTIONS.items():
            self.assertEqual(getattr(self.config_model, key), value)

    def test_set_options_if_valid_with_existing_file_and_valid_json_should_call_load_options(
        self,
    ):
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
        options_content = json.dumps(options)
        self.config_controller.load_options = MagicMock()
        with patch('builtins.open', create=True) as mock_open:
            with patch('os.path.exists', return_value=True):
                mock_open.return_value.read.return_value = options_content
                self.config_controller.set_options_if_valid()
                self.config_controller.load_options.assert_called_once_with(
                    options
                )

    @patch('os.path.exists', return_value=True)
    def test_set_options_if_valid_with_existing_file_and_invalid_json_should_call_set_default_options(
        self, _
    ):
        options = 'invalid json'
        self.config_controller.set_default_options = MagicMock()
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.read.return_value = options
            self.config_controller.set_options_if_valid()
            self.config_controller.set_default_options.assert_called_once()

    @patch('os.path.exists', return_value=True)
    def test_set_options_if_valid_with_existing_file_and_missing_keys_should_call_set_default_options(
        self, _
    ):
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
        }
        options_content = json.dumps(options)
        self.config_controller.set_default_options = MagicMock()
        with patch('builtins.open', create=True) as mock_open:
            mock_open.return_value.read.return_value = options_content
            self.config_controller.set_options_if_valid()
            self.config_controller.set_default_options.assert_called_once()

    @patch('os.path.exists', return_value=False)
    def test_set_options_if_valid_non_existing_file_should_call_set_default_options(
        self, _
    ):
        self.config_controller.set_default_options = MagicMock()
        self.config_controller.set_options_if_valid()
        self.config_controller.set_default_options.assert_called_once()

    def test_load_options_with_valid_params_should_update_config_model_properties(
        self,
    ):
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

        for key, value in options.items():
            self.assertEqual(getattr(self.config_model, key), value)

    def test_load_options_with_invalid_params_should_raise_attribute_error(
        self,
    ):
        options = {'invalid_key': 'invalid_value'}
        with self.assertRaises(AttributeError):
            self.config_controller.load_options(options)

    def test_save_options_with_valid_params_should_update_config_model_and_write_options_file_and_show_popup(
        self,
    ):
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
        with patch('builtins.open', create=True) as mock_open:
            mock_file = MagicMock()
            mock_open.return_value.__enter__.return_value = mock_file

            mock_signal = MagicMock()
            self.config_controller.show_popup_signal = mock_signal

            self.config_controller.save_options(options)

            for key, value in options.items():
                self.assertEqual(getattr(self.config_model, key), value)

            mock_file.write.assert_called_once_with(
                json.dumps(options, indent=4)
            )

            mock_signal.emit.assert_called_once_with(
                'Sucesso!', 'Configurações salvas com sucesso!'
            )

    def test_save_options_with_invalid_params_should_raise_attribute_error(
        self,
    ):
        options = {'invalid_key': 'invalid_value'}
        with self.assertRaises(AttributeError):
            self.config_controller.save_options(options)
