from src.interfaces.i_selectors import ISelectors
from src.selectors.lite_instagram_app import LiteInstagramSelectors
from src.selectors.official_instagram_app import OfficialInstagramSelectors


class SelectorsFactory:
    def create_selectors(self, automation_app: str) -> ISelectors:
        if automation_app == 'official_instagram':
            return OfficialInstagramSelectors()
        elif automation_app == 'lite_instagram':
            return LiteInstagramSelectors()
        else:
            raise ValueError('Invalid automation app')
