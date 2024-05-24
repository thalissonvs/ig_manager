from src.interfaces.i_ig_selectors import IIGSelectors


class LiteInstagramSelectors(IIGSelectors):
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
