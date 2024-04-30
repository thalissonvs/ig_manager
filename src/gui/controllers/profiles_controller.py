import _thread as thread
import time

from PyQt5.QtCore import QObject, pyqtSignal

from src.gui.models.profiles_model import ProfilesModel
from src.gui.services.profiles_service import ProfilesService


class ProfilesController(QObject):

    profile_added = pyqtSignal(dict)
    profile_removed = pyqtSignal(str)
    show_popup_signal = pyqtSignal(str, str)

    def __init__(
        self, profiles_model: ProfilesModel, profiles_service: ProfilesService
    ) -> None:
        super().__init__()
        self._profiles_model = profiles_model
        self._profiles_service = profiles_service
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

    def add_multiple_profiles(self, profiles_text: str) -> None:
        profiles = self._profiles_service.format_profiles_text(profiles_text)
        for profile in profiles:
            self.add_single_profile(**profile)
