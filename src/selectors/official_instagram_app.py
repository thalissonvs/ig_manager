from src.interfaces.i_ig_selectors import IIGSelectors


class OfficialInstagramSelectors(IIGSelectors):
    @property
    def APP_PACKAGE(self) -> str:
        return 'com.instagram.android'

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
            {'resourceId': 'com.instagram.android:id/login_username'},
            {
                'xpath': '//*[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.widget.EditText[1]',
            },
        ]

    @property
    def PASSWORD_INPUT(self) -> dict:
        return [
            {'resourceId': 'com.instagram.android:id/password'},
            {
                'xpath': '//*[@resource-id="com.instagram.android:id/layout_container_main"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[2]/android.widget.FrameLayout[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[1]/android.view.ViewGroup[2]/android.view.ViewGroup[1]/android.widget.EditText[1]',
            },
        ]

    @property
    def SUBMIT_BUTTON(self) -> dict:
        return [
            {
                'text': 'Entrar',
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

    @property
    def PROFILE_TAB(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/profile_tab',
                'description': 'Perfil',
            }
        ]

    @property
    def OPEN_PROFILES_LIST(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/action_bar_large_title_auto_size',
            }
        ]

    @property
    def PROFILES_USERNAMES(self) -> dict:
        return [
            {
                'xpath': '//*[@resource-id="com.instagram.android:id/recycler_view_container_id"]//android.view.View/all'
            }
        ]

    @property
    def PROFILE_OPTIONS(self) -> dict:
        return [
            {
                'description': 'Opções',
            }
        ]

    @property
    def LOGOUT_BUTTON(self) -> dict:
        return [
            {
                'text': 'Sair',
            }
        ]

    @property
    def ADD_NEW_ACCOUNT_BUTTON(self) -> dict:
        return [
            {
                'text': 'Adicionar conta do Instagram',
            }
        ]

    @property
    def EXISTENT_ACCOUNT_BUTTON(self) -> dict:
        return [
            {
                'text': 'Entrar na conta existente',
            }
        ]

    @property
    def CHANGE_ACCOUNT_BUTTON(self) -> dict:
        return [
            {
                'text': 'Trocar de conta',
            }
        ]

    @property
    def POPUPS(self) -> dict:
        return [
            {
                'text': 'Agora não',
            },
            {'text': 'NÃO PERMITIR'},
        ]

    @property
    def IS_NO_ACCOUNT_LOGGED(self) -> dict:
        return [
            *self.SUBMIT_BUTTON,
            *self.LOGIN_INTO_ANOTHER_ACCOUNT,
        ]

    @property
    def DISCONNECTED_ACCOUNT(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/primary_button',
                'text': 'OK',
            },
        ]

    @property
    def CURRENT_ACCOUNT(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/action_bar_large_title_auto_size',
            }
        ]

    @property
    def COMMENT_BUTTON(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/row_feed_button_comment',
            }
        ]

    @property
    def COMMENT_INPUT(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/layout_comment_thread_edittext',
            }
        ]

    @property
    def POST_COMMENT_BUTTON(self) -> dict:
        return [
            {
                'resourceId': 'com.instagram.android:id/layout_comment_thread_post_button_icon',
            }
        ]
