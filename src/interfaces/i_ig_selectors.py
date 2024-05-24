from abc import ABC


class IIGSelectors(ABC):
    @property
    def APP_PACKAGE(self) -> str:
        pass

    @property
    def LOGIN_INTO_ANOTHER_ACCOUNT(self) -> dict:
        pass

    @property
    def USERNAME_INPUT(self) -> dict:
        pass

    @property
    def PASSWORD_INPUT(self) -> dict:
        pass

    @property
    def SUBMIT_BUTTON(self) -> dict:
        pass

    @property
    def LOGIN_VERIFIER(self) -> dict:
        pass

    @property
    def PROFILE_TAB(self) -> dict:
        pass

    @property
    def OPEN_PROFILES_LIST(self) -> dict:
        pass

    @property
    def PROFILES_USERNAMES(self) -> dict:
        pass

    @property
    def PROFILE_OPTIONS(self) -> dict:
        pass

    @property
    def LOGOUT_BUTTON(self) -> dict:
        pass

    @property
    def ADD_NEW_ACCOUNT_BUTTON(self) -> dict:
        pass

    @property
    def EXISTENT_ACCOUNT_BUTTON(self) -> dict:
        pass

    @property
    def CHANGE_ACCOUNT_BUTTON(self) -> dict:
        pass

    @property
    def POPUPS(self) -> dict:
        pass

    @property
    def IS_NO_ACCOUNT_LOGGED(self) -> dict:
        pass

    @property
    def DISCONNECTED_ACCOUNT(self) -> dict:
        pass

    @property
    def CURRENT_ACCOUNT(self) -> dict:
        pass

    @property
    def COMMENT_BUTTON(self) -> dict:
        pass

    @property
    def COMMENT_INPUT(self) -> dict:
        pass

    @property
    def POST_COMMENT_BUTTON(self) -> dict:
        pass
