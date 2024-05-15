from PyQt5.QtCore import QObject, pyqtSignal

from src.gui.models.profile_model import ProfileModel


class GroupModel(QObject):
    def __init__(self) -> None:
        super().__init__()
        self._group_name = None
        self._device_id = None
        self._index = None
        self.max_profiles = 5
        self._profiles: list[ProfileModel] = []

    def get_group_info(self) -> dict:
        return {
            'group_name': self.group_name,
            'device_id': self.device_id,
            'index': self.index,
            'profiles': [
                profile.get_profile_info() for profile in self.profiles
            ],
        }

    def add_profile(
        self,
        username: str,
        password: str,
        gender: str,
        like_actions_done: int = 0,
        follow_actions_done: int = 0,
        comment_actions_done: int = 0,
        status: str = 'active',
        current_log: str = 'Aguardando início...',
    ) -> None:

        if len(self._profiles) >= self.max_profiles:
            raise Exception('Max profiles reached')

        profile = ProfileModel()
        profile.username = username
        profile.password = password
        profile.gender = gender
        profile.like_actions_done = like_actions_done
        profile.follow_actions_done = follow_actions_done
        profile.comment_actions_done = comment_actions_done
        profile.status = status
        profile.current_log = current_log
        self._profiles.append(profile)

    @property
    def group_name(self) -> str:
        return self._group_name

    @group_name.setter
    def group_name(self, value: str) -> None:
        self._group_name = value

    @property
    def device_id(self) -> str:
        return self._device_id

    @device_id.setter
    def device_id(self, value: str) -> None:
        self._device_id = value

    @property
    def index(self) -> int:
        return self._index

    @index.setter
    def index(self, value: int) -> None:
        self._index = value

    @property
    def profiles(self) -> list[ProfileModel]:
        return self._profiles

    @profiles.setter
    def profiles(self, value: ProfileModel) -> None:
        self._profiles = value


class GroupsModel(QObject):

    group_added = pyqtSignal(dict)
    group_removed = pyqtSignal(int)
    profile_added = pyqtSignal(dict)
    profile_removed = pyqtSignal(str)
    profile_edited = pyqtSignal(str, dict)

    def __init__(self) -> None:
        super().__init__()
        self._groups: list[GroupModel] = []

    def get_group_model(self, group_index: int) -> GroupModel:
        return self._groups[group_index]

    def get_groups(self) -> list:
        return [group.get_group_info() for group in self._groups]

    def get_group(self, group_index: int) -> dict:
        return self._groups[group_index].get_group_info()

    def create_group(self, group_name: str, device_id: str) -> None:
        group = GroupModel()
        group.group_name = group_name
        group.device_id = device_id
        group.index = len(self._groups)
        self._groups.append(group)
        self.group_added.emit(group.get_group_info())

    def add_profile_to_group(
        self, group_index: int, username: str, password: str, gender: str
    ) -> None:
        group = self._groups[group_index]
        group.add_profile(username, password, gender)
        self.profile_added.emit(group.profiles[-1].get_profile_info())

    def remove_profile_from_group(
        self, group_index: int, profile_username: str
    ) -> None:
        group = self._groups[group_index]
        profile = self._get_profile_model(group_index, profile_username)
        group.profiles.remove(profile)
        self.profile_removed.emit(profile_username)

    def remove_group(self, group_index: int) -> None:
        self._groups.pop(group_index)
        self.group_removed.emit(group_index)

    def edit_group(
        self, group_index: int, new_name: str, device_id: str
    ) -> None:
        group = self._groups[group_index]
        group.group_name = new_name
        group.device_id = device_id
        self.group_added.emit(group.get_group_info())

    def get_profiles_list_info_from_group(self, group_index: int) -> list:
        return self._groups[group_index].profiles

    def get_profile_info_from_group(
        self, group_index: int, profile_username: str
    ) -> dict:
        profile = self._get_profile_model(group_index, profile_username)
        if profile:
            return profile.get_profile_info()
        return None

    def edit_profile_data_from_group(
        self,
        group_index: int,
        profile_username: str,
        new_username: str,
        new_password: str,
        new_gender: str,
    ) -> None:
        profile = self._get_profile_model(group_index, profile_username)
        if profile:
            profile.username = new_username
            profile.password = new_password
            profile.gender = new_gender
            self.profile_edited.emit(
                profile_username, profile.get_profile_info()
            )

    def edit_profile_actions_done_from_group(
        self,
        group_index: int,
        profile_username: str,
        like_actions_done: int,
        follow_actions_done: int,
        comment_actions_done: int,
    ) -> None:
        profile = self._get_profile_model(group_index, profile_username)
        if profile:
            profile.like_actions_done = like_actions_done
            profile.follow_actions_done = follow_actions_done
            profile.comment_actions_done = comment_actions_done
            self.profile_edited.emit(
                profile_username, profile.get_profile_info()
            )

    def edit_profile_status_from_group(
        self, group_index: int, profile_username: str, status: str
    ) -> None:
        profile = self._get_profile_model(group_index, profile_username)
        if profile:
            profile.status = status
            self.profile_edited.emit(
                profile_username, profile.get_profile_info()
            )

    def edit_profile_current_log_from_group(
        self, group_index: int, profile_username: str, current_log: str
    ) -> None:
        profile = self._get_profile_model(group_index, profile_username)
        if profile:
            profile.current_log = current_log
            self.profile_edited.emit(
                profile_username, profile.get_profile_info()
            )

    def _get_profile_model(
        self, group_index: int, profile_username: str
    ) -> ProfileModel:
        group = self._groups[group_index]
        for profile in group.profiles:
            if profile.username == profile_username:
                return profile
        return None
