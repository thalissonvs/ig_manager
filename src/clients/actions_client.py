import requests


class ActionsClient:

    BASE_URL = 'http://api.provedorsmm.digital/api/comments/'

    def __init__(self) -> None:
        self.session = requests.Session()

    def add_profile(self, profile: str, password: str) -> dict:
        response = self.session.post(
            self.BASE_URL + 'add-profile',
            data={'profile': profile, 'password': password},
        )
        return response.json()

    def get_action(self, profile: str) -> dict:
        response = self.session.post(
            self.BASE_URL + 'get-action', data={'profile': profile}
        )
        return response.json()

    def confirm_action(
        self, profile: str, order: int, comment_id: int
    ) -> dict:
        response = self.session.post(
            self.BASE_URL + 'confirm-action',
            data={'profile': profile, 'order': order, 'commendId': comment_id},
        )
        return response.json()
