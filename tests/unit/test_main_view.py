import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch

from PyQt5.QtWidgets import QApplication, QMessageBox

from src.gui.constants import OptionsKeys
from src.gui.views.main_view import MainView


class TestMainView(TestCase):

    SIGNALS = [
        'time_between_actions_min_changed',
        'time_between_actions_max_changed',
        'actions_to_switch_account_changed',
        'switch_account_with_no_tasks_changed',
        'time_without_tasks_to_wait_changed',
        'perform_like_actions_changed',
        'perform_follow_actions_changed',
        'enable_goal_changed',
        'actions_goal_changed',
        'enable_rest_goal_changed',
        'rest_goal_actions_changed',
        'rest_goal_time_changed',
    ]

    SET_METHODS = [
        'set_time_between_actions_min_value',
        'set_time_between_actions_max_value',
        'set_actions_to_switch_account_value',
        'set_switch_account_with_no_tasks_value',
        'set_time_without_tasks_to_wait_value',
        'set_perform_like_actions_value',
        'set_perform_follow_actions_value',
        'set_enable_goal_value',
        'set_actions_goal_value',
        'set_enable_rest_goal_value',
        'set_rest_goal_actions_value',
        'set_rest_goal_time_value',
    ]

    def setUp(self) -> None:
        self.app = QApplication(sys.argv)
        self.config_model = MagicMock()
        self.config_controller = MagicMock()
        self.main_view = MainView(self.config_model, self.config_controller)

    def test_save_options_should_call_config_controller_save_options(
        self,
    ) -> None:
        self.main_view.get_options_object = MagicMock(return_value={})
        self.main_view.save_options()
        self.config_controller.save_options.assert_called_once_with({})

    def test_get_options_object_should_return_expected_object(self) -> None:
        self.main_view.get_time_between_actions_min_value = MagicMock(
            return_value=1
        )
        self.main_view.get_time_between_actions_max_value = MagicMock(
            return_value=2
        )
        self.main_view.get_actions_to_switch_account_value = MagicMock(
            return_value=3
        )
        self.main_view.get_switch_account_with_no_tasks_value = MagicMock(
            return_value=True
        )
        self.main_view.get_time_without_tasks_to_wait_value = MagicMock(
            return_value=4
        )
        self.main_view.get_perform_like_actions_value = MagicMock(
            return_value=True
        )
        self.main_view.get_perform_follow_actions_value = MagicMock(
            return_value=True
        )
        self.main_view.get_enable_goal_value = MagicMock(return_value=True)
        self.main_view.get_actions_goal_value = MagicMock(return_value=5)
        self.main_view.get_enable_rest_goal_value = MagicMock(
            return_value=True
        )
        self.main_view.get_rest_goal_actions_value = MagicMock(return_value=6)
        self.main_view.get_rest_goal_time_value = MagicMock(return_value=7)

        expected = {
            OptionsKeys.TIME_BETWEEN_ACTIONS_MIN: 1,
            OptionsKeys.TIME_BETWEEN_ACTIONS_MAX: 2,
            OptionsKeys.ACTIONS_TO_SWITCH_ACCOUNT: 3,
            OptionsKeys.SWITCH_ACCOUNT_WITH_NO_TASKS: True,
            OptionsKeys.TIME_WITHOUT_TASKS_TO_WAIT: 4,
            OptionsKeys.PERFORM_LIKE_ACTIONS: True,
            OptionsKeys.PERFORM_FOLLOW_ACTIONS: True,
            OptionsKeys.ENABLE_GOAL: True,
            OptionsKeys.ACTIONS_GOAL: 5,
            OptionsKeys.ENABLE_REST_GOAL: True,
            OptionsKeys.REST_GOAL_ACTIONS: 6,
            OptionsKeys.REST_GOAL_TIME: 7,
        }

        self.assertEqual(self.main_view.get_options_object(), expected)

    @patch('src.gui.views.main_view.QMessageBox')
    def test_show_popup(self, message_box_mock) -> None:
        message = 'title'
        text = 'text'

        self.main_view.show_popup(message, text)
        message_box_mock.assert_called_once()
        message_box_mock().setWindowTitle.assert_called_once_with(message)
        message_box_mock().setText.assert_called_once_with(text)
        message_box_mock().setIcon.assert_called_once_with(
            message_box_mock.Information
        )
        message_box_mock().exec_.assert_called_once()

    def test_connect_config_model_signals_should_connect_all_config_model_signals(
        self,
    ) -> None:

        for signal in self.SIGNALS:
            setattr(self.config_model, signal, MagicMock())

        self.main_view.connect_config_model_signals()

        for signal in self.SIGNALS:
            getattr(self.config_model, signal).connect.assert_called_once()
            getattr(self.config_model, signal).connect.assert_called_once_with(
                getattr(
                    self.main_view,
                    self.SET_METHODS[self.SIGNALS.index(signal)],
                )
            )

    def test_set_time_between_actions_min_value(self) -> None:
        value = 10
        self.main_view.set_time_between_actions_min_value(value)
        self.assertEqual(
            self.main_view.spinbox_min_time_actions.value(), value
        )

    def test_set_time_between_actions_max_value(self) -> None:
        value = 10
        self.main_view.set_time_between_actions_max_value(value)
        self.assertEqual(
            self.main_view.spinbox_max_time_actions.value(), value
        )

    def test_set_actions_to_switch_account_value(self) -> None:
        value = 10
        self.main_view.set_actions_to_switch_account_value(value)
        self.assertEqual(
            self.main_view.spinbox_actions_change_amount.value(), value
        )

    def test_set_switch_account_with_no_tasks_value(self) -> None:
        value = True
        self.main_view.set_switch_account_with_no_tasks_value(value)
        self.assertEqual(
            self.main_view.radiobutton_change_actions.isChecked(), value
        )
        self.assertEqual(
            self.main_view.radiobutton_dont_change_actions.isChecked(),
            not value,
        )

    def test_set_time_without_tasks_to_wait_value(self) -> None:
        value = 10
        self.main_view.set_time_without_tasks_to_wait_value(value)
        self.assertEqual(
            self.main_view.spinbox_seconds_to_change.value(), value
        )

    def test_set_perform_like_actions_value(self) -> None:
        value = True
        self.main_view.set_perform_like_actions_value(value)
        self.assertEqual(self.main_view.checkbox_like.isChecked(), value)

    def test_set_perform_follow_actions_value(self) -> None:
        value = True
        self.main_view.set_perform_follow_actions_value(value)
        self.assertEqual(self.main_view.checkbox_follow.isChecked(), value)

    def test_set_enable_goal_value(self) -> None:
        value = True
        self.main_view.set_enable_goal_value(value)
        self.assertEqual(
            self.main_view.radiobutton_enable_goal.isChecked(), value
        )
        self.assertEqual(
            self.main_view.radiobutton_disable_goal.isChecked(), not value
        )

    def test_set_actions_goal_value(self) -> None:
        value = 10
        self.main_view.set_actions_goal_value(value)
        self.assertEqual(self.main_view.spinbox_goal_actions.value(), value)

    def test_set_enable_rest_goal_value(self) -> None:
        value = True
        self.main_view.set_enable_rest_goal_value(value)
        self.assertEqual(
            self.main_view.radiobutton_enable_rest_goal.isChecked(), value
        )
        self.assertEqual(
            self.main_view.radiobutton_disable_rest_goal.isChecked(), not value
        )

    def test_set_rest_goal_actions_value(self) -> None:
        value = 10
        self.main_view.set_rest_goal_actions_value(value)
        self.assertEqual(self.main_view.spinbox_actions_rest.value(), value)

    def test_set_rest_goal_time_value(self) -> None:
        value = 10
        self.main_view.set_rest_goal_time_value(value)
        self.assertEqual(self.main_view.spinbox_minutes_rest.value(), value)

    def test_get_time_between_actions_min_value(self) -> None:
        value = 10
        self.main_view.spinbox_min_time_actions.setValue(value)
        self.assertEqual(
            self.main_view.get_time_between_actions_min_value(), value
        )

    def test_get_time_between_actions_max_value(self) -> None:
        value = 10
        self.main_view.spinbox_max_time_actions.setValue(value)
        self.assertEqual(
            self.main_view.get_time_between_actions_max_value(), value
        )

    def test_get_actions_to_switch_account_value(self) -> None:
        value = 10
        self.main_view.spinbox_actions_change_amount.setValue(value)
        self.assertEqual(
            self.main_view.get_actions_to_switch_account_value(), value
        )

    def test_get_switch_account_with_no_tasks_value(self) -> None:
        value = True
        self.main_view.radiobutton_change_actions.setChecked(value)
        self.assertEqual(
            self.main_view.get_switch_account_with_no_tasks_value(), value
        )

    def test_get_time_without_tasks_to_wait_value(self) -> None:
        value = 10
        self.main_view.spinbox_seconds_to_change.setValue(value)
        self.assertEqual(
            self.main_view.get_time_without_tasks_to_wait_value(), value
        )

    def test_get_perform_like_actions_value(self) -> None:
        value = True
        self.main_view.checkbox_like.setChecked(value)
        self.assertEqual(
            self.main_view.get_perform_like_actions_value(), value
        )

    def test_get_perform_follow_actions_value(self) -> None:
        value = True
        self.main_view.checkbox_follow.setChecked(value)
        self.assertEqual(
            self.main_view.get_perform_follow_actions_value(), value
        )

    def test_get_enable_goal_value(self) -> None:
        value = True
        self.main_view.radiobutton_enable_goal.setChecked(value)
        self.assertEqual(self.main_view.get_enable_goal_value(), value)

    def test_get_actions_goal_value(self) -> None:
        value = 10
        self.main_view.spinbox_goal_actions.setValue(value)
        self.assertEqual(self.main_view.get_actions_goal_value(), value)

    def test_get_enable_rest_goal_value(self) -> None:
        value = True
        self.main_view.radiobutton_enable_rest_goal.setChecked(value)
        self.assertEqual(self.main_view.get_enable_rest_goal_value(), value)

    def test_get_rest_goal_actions_value(self) -> None:
        value = 10
        self.main_view.spinbox_actions_rest.setValue(value)
        self.assertEqual(self.main_view.get_rest_goal_actions_value(), value)

    def test_get_rest_goal_time_value(self) -> None:
        value = 10
        self.main_view.spinbox_minutes_rest.setValue(value)
        self.assertEqual(self.main_view.get_rest_goal_time_value(), value)
