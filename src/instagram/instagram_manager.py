from src.interfaces.i_automator import IAutomator
from src.interfaces.i_selectors import ISelectors


class InstagramManager:

    DEFAULT_TIMEOUT = 15

    def __init__(self, automator: IAutomator, selectors: ISelectors) -> None:
        self.automator = automator
        self.selectors = selectors

    def login(self, username: str, password: str) -> bool:
        self.automator.click(self.selectors.LOGIN_BUTTON, self.DEFAULT_TIMEOUT)
        self.automator.send_keys(self.selectors.USERNAME_INPUT, username)
        self.automator.send_keys(self.selectors.PASSWORD_INPUT, password)
        self.automator.click(
            self.selectors.SUBMIT_BUTTON, self.DEFAULT_TIMEOUT
        )
        return self.verify_login()
