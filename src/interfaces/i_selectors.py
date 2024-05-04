from abc import ABC


class ISelectors(ABC):
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