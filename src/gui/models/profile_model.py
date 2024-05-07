from PyQt5.QtCore import QObject, pyqtSignal


class ProfileModel(QObject):
    def __init__(self) -> None:
        super().__init__()
        self._username = None
        self._password = None
        self._gender = None
        self._like_actions_done = None
        self._follow_actions_done = None
        self._comment_actions_done = None
        self._status = None
        self._current_log = None

    def get_profile_info(self) -> dict:
        return {
            'username': self.username,
            'password': self.password,
            'gender': self.gender,
            'like_actions_done': self.like_actions_done,
            'follow_actions_done': self.follow_actions_done,
            'comment_actions_done': self.comment_actions_done,
            'status': self.status,
            'current_log': self.current_log,
        }

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        self._username = value

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, value: str) -> None:
        self._password = value

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, value: str) -> None:
        self._gender = value

    @property
    def like_actions_done(self) -> int:
        return self._like_actions_done

    @like_actions_done.setter
    def like_actions_done(self, value: int) -> None:
        self._like_actions_done = value

    @property
    def follow_actions_done(self) -> int:
        return self._follow_actions_done

    @follow_actions_done.setter
    def follow_actions_done(self, value: int) -> None:
        self._follow_actions_done = value

    @property
    def comment_actions_done(self) -> int:
        return self._comment_actions_done

    @comment_actions_done.setter
    def comment_actions_done(self, value: int) -> None:
        self._comment_actions_done = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        self._status = value

    @property
    def current_log(self) -> str:
        return self._current_log

    @current_log.setter
    def current_log(self, value: str) -> None:
        self._current_log = value
