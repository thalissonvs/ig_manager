from abc import ABC


class ISelectors(ABC):
    @property
    def LOGIN_BUTTON(self) -> str:
        pass

    @property
    def USERNAME_INPUT(self) -> str:
        pass

    @property
    def PASSWORD_INPUT(self) -> str:
        pass

    @property
    def SUBMIT_BUTTON(self) -> str:
        pass
