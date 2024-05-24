from PyQt5.QtCore import QObject, pyqtSignal

from src.gui.models.groups_model import GroupsModel
from src.gui.repository.groups_repository import GroupsRepository
from src.gui.services.profiles_formatter_service import \
    ProfilesFormatterService


class GroupsController(QObject):

    group_added = pyqtSignal(dict)
    group_removed = pyqtSignal(int)
    group_edited = pyqtSignal(dict)

    profile_added = pyqtSignal(dict)
    profile_removed = pyqtSignal(str)
    profile_edited = pyqtSignal(str, dict)

    current_account_changed = pyqtSignal(int, str)

    show_popup_signal = pyqtSignal(str, str)

    def __init__(
        self,
        groups_model: GroupsModel,
        groups_repository: GroupsRepository,
    ) -> None:
        super().__init__()
        self._groups_model = groups_model
        self._groups_repository = groups_repository

        self._groups_model.group_added.connect(self._emit_group_added)
        self._groups_model.group_removed.connect(self._emit_group_removed)
        self._groups_model.group_edited.connect(self._emit_group_edited)

        self._groups_model.profile_added.connect(self._emit_profile_added)
        self._groups_model.profile_removed.connect(self._emit_profile_removed)
        self._groups_model.profile_edited.connect(self._emit_profile_edited)

        self._groups_model.current_account_changed.connect(
            self._emit_current_account_changed
        )

    def _emit_group_edited(self, group_info: dict) -> None:
        self.group_edited.emit(group_info)

    def _emit_group_added(self, group_info: dict) -> None:
        self.group_added.emit(group_info)

    def _emit_group_removed(self, group_index: int) -> None:
        self.group_removed.emit(group_index)

    def _emit_profile_added(self, profile_info: dict) -> None:
        self.profile_added.emit(profile_info)

    def _emit_profile_removed(self, username: str) -> None:
        self.profile_removed.emit(username)

    def _emit_profile_edited(
        self, old_username: str, profile_info: dict
    ) -> None:
        self.profile_edited.emit(old_username, profile_info)

    def _emit_current_account_changed(
        self, group_index, username: str
    ) -> None:
        self.current_account_changed.emit(group_index, username)

    def get_groups_info(self) -> list:
        return self._groups_model.get_groups_info()

    def get_group_info(self, group_index: int) -> dict:
        return self._groups_model.get_group_info(group_index)

    def create_group(
        self,
        group_name: str,
        device_id: str,
    ) -> None:
        self._groups_model.create_group(group_name, device_id)
        groups = self._groups_model.get_groups_info()
        self._groups_repository.set_groups(groups)

    def remove_group(self, group_index: int) -> None:
        self._groups_model.remove_group(group_index)
        groups = self._groups_model.get_groups_info()
        self._groups_repository.set_groups(groups)

    def edit_group(
        self, group_index: int, new_name: str, device_id: str
    ) -> None:
        self._groups_model.edit_group(group_index, new_name, device_id)
        groups = self._groups_model.get_groups_info()
        self._groups_repository.set_groups(groups)

    def edit_group_current_log(
        self, group_index: int, current_log: str
    ) -> None:
        self._groups_model.edit_group_current_log(group_index, current_log)

    def add_profile_to_group(
        self, group_index: int, username: str, password: str, gender: str
    ) -> None:
        self._groups_model.add_profile_to_group(
            group_index, username, password, gender
        )
        groups = self._groups_model.get_groups_info()
        self._groups_repository.set_groups(groups)

    def add_multiples_profiles_to_group(
        self, group_index: int, profiles_text: str
    ) -> None:
        profiles = ProfilesFormatterService.format_profiles_text(profiles_text)
        for profile in profiles:
            self.add_profile_to_group(
                group_index,
                profile['username'],
                profile['password'],
                profile['gender'],
            )

    def remove_profile_from_group(
        self, group_index: int, profile_username: str
    ) -> None:
        self._groups_model.remove_profile_from_group(
            group_index, profile_username
        )
        groups = self._groups_model.get_groups_info()
        self._groups_repository.set_groups(groups)

    def get_group_profile_info(
        self, group_index: int, profile_username: str
    ) -> dict:
        return self._groups_model.get_group_profile_info(
            group_index, profile_username
        )

    def edit_group_profile_data(
        self,
        group_index: int,
        profile_username: str,
        new_username: str,
        new_password: str,
        gender: str,
    ) -> None:
        self._groups_model.edit_group_profile_data(
            group_index, profile_username, new_username, new_password, gender
        )
        groups = self._groups_model.get_groups_info()
        self._groups_repository.set_groups(groups)

    def edit_group_profile_actions_done(
        self,
        group_index: int,
        profile_username: str,
        like_actions_done: int,
        follow_actions_done: int,
        comment_actions_done: int,
    ) -> None:
        self._groups_model.edit_group_profile_actions_done(
            group_index,
            profile_username,
            like_actions_done,
            follow_actions_done,
            comment_actions_done,
        )
        groups = self._groups_model.get_groups_info()
        self._groups_repository.set_groups(groups)

    def set_repository_to_model(self) -> None:
        groups = self._groups_repository.get_groups()
        for group in groups:
            self._groups_model.create_group(
                group['group_name'], group['device_id']
            )
            for profile in group['profiles']:
                self._groups_model.add_profile_to_group(
                    group['index'],
                    profile['username'],
                    profile['password'],
                    profile['gender'],
                )
