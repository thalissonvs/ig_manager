import _thread as thread
import time

from PyQt5.QtCore import QObject, pyqtSignal

from src.gui.models.profiles_model import ProfilesModel
from src.gui.repository.profiles_repository import ProfilesRepository
from src.gui.services.profiles_service import ProfilesService


class ProfilesController(QObject):

    profile_added = pyqtSignal(dict)
    profile_removed = pyqtSignal(str)
    show_popup_signal = pyqtSignal(str, str)

    def __init__(
        self,
        profiles_model: ProfilesModel,
        profiles_service: ProfilesService,
        profiles_repository: ProfilesRepository,
    ) -> None:
        super().__init__()
        self._profiles_model = profiles_model
        self._profiles_service = profiles_service
        self._profiles_repository = profiles_repository
        self._profiles_model.profile_added.connect(self._emit_profile_added)
        self._profiles_model.profile_removed.connect(
            self._emit_profile_removed
        )

    def _emit_profile_added(self, profile_info: dict) -> None:
        self.profile_added.emit(profile_info)

    def _emit_profile_removed(self, profile_username: str) -> None:
        self.profile_removed.emit(profile_username)

    def add_single_profile(
        self,
        username: str,
        password: str,
        gender: str,
    ) -> None:
        self._profiles_model.add_profile(username, password, gender)
        self._profiles_repository.add_new_profile(
            self._profiles_model.get_profile(username)
        )

    def add_multiple_profiles(self, profiles_text: str) -> None:
        profiles = self._profiles_service.format_profiles_text(profiles_text)
        for profile in profiles:
            self.add_single_profile(**profile)

    def add_initial_profiles(self) -> None:
        profiles = self._profiles_repository.get_profiles()
        for profile in profiles.values():
            self._profiles_model.add_profile(**profile)

    def edit_profile(
        self, old_username: str, new_username: str, password: str, gender: str
    ) -> None:
        self._profiles_model.edit_profile(
            old_username, new_username, password, gender
        )
        self._profiles_repository.edit_profile(
            old_username, new_username, password, gender
        )

    def remove_profile(self, username: str) -> None:
        self._profiles_model.remove_profile(username)
        self._profiles_repository.remove_profile(username)
