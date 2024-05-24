import _thread as thread
import time

from src.automators.android_automator import AndroidAutomator
from src.interfaces.i_ig_selectors import IIGSelectors
from src.interfaces.i_manager import IManager


class InstagramManager(IManager):

    DEFAULT_TIMEOUT = 15

    def __init__(
        self, android_automator: AndroidAutomator, selectors: IIGSelectors
    ) -> None:
        self.android_automator = android_automator
        self.selectors = selectors

    def prepare(self) -> None:
        self.start_close_popups()
        return self.android_automator.open_app(self.selectors.APP_PACKAGE)

    def close_popups(self) -> None:
        while 1:
            try:
                self.android_automator.click(self.selectors.POPUPS, 5)
            except Exception:
                pass

    def start_close_popups(self) -> None:
        thread.start_new_thread(self.close_popups, ())

    def login(self, username: str, password: str) -> bool:
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
            self.selectors.LOGIN_VERIFIER, 15
        )
        if login_verifier is not None:
            if (
                'description' in login_verifier.info
                and login_verifier.info['description'] == 'Agora não'
            ):
                login_verifier.click()

            # antes de retornar True, verifica se a conta não foi desconectada
            disconnected_account = self.android_automator.find_element(
                self.selectors.DISCONNECTED_ACCOUNT, 5
            )
            if disconnected_account is not None:
                disconnected_account.click(timeout=5)
                return False
            return True

        return False

    def add_new_account(self) -> bool:
        try:
            self.android_automator.click(
                self.selectors.PROFILE_TAB, self.DEFAULT_TIMEOUT
            )
            self.android_automator.click(
                self.selectors.OPEN_PROFILES_LIST, self.DEFAULT_TIMEOUT
            )
            self.android_automator.click(
                self.selectors.ADD_NEW_ACCOUNT_BUTTON, self.DEFAULT_TIMEOUT
            )
            self.android_automator.click(
                self.selectors.EXISTENT_ACCOUNT_BUTTON, self.DEFAULT_TIMEOUT
            )
            self.android_automator.click(
                self.selectors.CHANGE_ACCOUNT_BUTTON, self.DEFAULT_TIMEOUT
            )
            return True
        except Exception:
            return False

    def get_logged_accounts(self) -> list:
        self.android_automator.restart_app(self.selectors.APP_PACKAGE)
        self.android_automator.click(
            self.selectors.PROFILE_TAB, self.DEFAULT_TIMEOUT
        )
        self.android_automator.click(
            self.selectors.OPEN_PROFILES_LIST, self.DEFAULT_TIMEOUT
        )
        time.sleep(3)
        profiles_usernames_views = self.android_automator.find_element(
            self.selectors.PROFILES_USERNAMES, self.DEFAULT_TIMEOUT
        )

        profiles_usernames = []
        for profile_username_view in profiles_usernames_views:
            text = profile_username_view.info['text']
            profiles_usernames.append(
                text
            ) if ' ' not in text.strip() else None

        self.android_automator.press_back()
        return profiles_usernames

    def change_to_account(self, username: str) -> bool:
        self.android_automator.click(
            self.selectors.PROFILE_TAB, self.DEFAULT_TIMEOUT
        )
        if self._is_account_already_selected(username):
            return True
        self.android_automator.click(
            self.selectors.OPEN_PROFILES_LIST, self.DEFAULT_TIMEOUT
        )
        profiles_usernames_views = self.android_automator.find_element(
            self.selectors.PROFILES_USERNAMES, self.DEFAULT_TIMEOUT
        )

        for profile_username_view in profiles_usernames_views:
            if profile_username_view.info['text'] == username:
                profile_username_view.click()
                return True

        return False

    def logout(self, username: str) -> bool:
        if not self.change_to_account(username):
            return False

        self.android_automator.click(
            self.selectors.PROFILE_OPTIONS, self.DEFAULT_TIMEOUT
        )
        self.android_automator.scroll_down(200)

        self.android_automator.click(
            self.selectors.LOGOUT_BUTTON, self.DEFAULT_TIMEOUT
        )

        return True

    def is_no_account_logged(self) -> bool:
        no_account_logged = self.android_automator.find_element(
            self.selectors.IS_NO_ACCOUNT_LOGGED, 5
        )

        if no_account_logged is not None:
            return True
        return False

    def follow(self, username: str) -> bool:
        pass

    def like(self, link: str) -> bool:
        pass

    def comment(self, link: str, comment: str) -> bool:
        self.android_automator.execute_adb_command(
            f'am start -a android.intent.action.VIEW -d {link} {self.selectors.APP_PACKAGE}'
        )
        self.android_automator.click(
            self.selectors.COMMENT_BUTTON, self.DEFAULT_TIMEOUT
        )
        self.android_automator.click(
            self.selectors.COMMENT_INPUT, self.DEFAULT_TIMEOUT
        )
        self.android_automator.send_keys(self.selectors.COMMENT_INPUT, comment)
        time.sleep(2)
        self.android_automator.click(
            self.selectors.POST_COMMENT_BUTTON, self.DEFAULT_TIMEOUT
        )
        return True

    def _is_account_already_selected(self, username: str) -> bool:
        current_account_view = self.android_automator.find_element(
            self.selectors.CURRENT_ACCOUNT, 5
        )
        if (
            current_account_view is not None
            and current_account_view.info['text'] == username
        ):
            return True
        return False
