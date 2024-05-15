from src.interfaces.i_selectors import ISelectors


class OfficialInstagramSelectors(ISelectors):
    @property
    def LOGIN_INTO_ANOTHER_ACCOUNT(self) -> dict:
        return [
            {
                'className': 'android.widget.Button',
                'description': 'Entrar em outra conta',
            }
        ]

    @property
    def USERNAME_INPUT(self) -> dict:
        return [
            {
                'xpath': '//android.view.ViewGroup[1]//android.widget.EditText'
            }
        ]

    @property
    def PASSWORD_INPUT(self) -> dict:
        return [
            {
                'xpath': '//android.view.ViewGroup[2]//android.widget.EditText'
            }
        ]

    @property
    def SUBMIT_BUTTON(self) -> dict:
        return [
            {
                'className': 'android.view.View',
                'text': 'Entrar',
                'description': 'Entrar',
            }
        ]

    @property
    def LOGIN_VERIFIER(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/avatar_image_view',
            },
            {
                'description': 'Agora não',
                'className': 'android.widget.Button',
            },
        ]
