import _thread as thread
import time

from src.automators.android_automator import AndroidAutomator
from src.interfaces.i_manager import IManager
from src.interfaces.i_selectors import ISelectors


class InstagramManager(IManager):

    DEFAULT_TIMEOUT = 15

    def __init__(
        self, android_automator: AndroidAutomator, selectors: ISelectors
    ) -> None:
        self.android_automator = android_automator
        self.selectors = selectors

    def login(self, username: str, password: str) -> bool:
        self.android_automator.prepare()
        try:
            self.android_automator.click(
                self.selectors.LOGIN_INTO_ANOTHER_ACCOUNT, 5
            )
        except Exception:
            pass
        self.android_automator.send_keys(
            self.selectors.USERNAME_INPUT, username
        )
        self.android_automator.send_keys(
            self.selectors.PASSWORD_INPUT, password
        )
        self.android_automator.click(
            self.selectors.SUBMIT_BUTTON, self.DEFAULT_TIMEOUT
        )
        return self.verify_login()

    def verify_login(self) -> bool:
        login_verifier = self.android_automator.find_element(
            self.selectors.LOGIN_VERIFIER
        )
        try:
            self.android_automator.wait_for_element(
                login_verifier, self.DEFAULT_TIMEOUT
            )
            return True
        except TimeoutError:
            return False

    def follow(self, username: str) -> bool:
        pass

    def like(self, link: str) -> bool:
        pass

    def comment(self, link: str, comment: str) -> bool:
        pass
