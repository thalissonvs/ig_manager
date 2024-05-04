from src.interfaces.i_selectors import ISelectors


class LiteInstagramSelectors(ISelectors):
    @property
    def LOGIN_BUTTON(self) -> dict:
        return {'resourceId': 'com.instagram.android:id/log_in_button'}

    @property
    def USERNAME_INPUT(self) -> dict:
        return {'resourceId': 'com.instagram.android:id/login_username'}

    @property
    def PASSWORD_INPUT(self) -> dict:
        return {'resourceId': 'com.instagram.android:id/password'}

    @property
    def SUBMIT_BUTTON(self) -> dict:
        return {'resourceId': 'com.instagram.android:id/next_button'}
