from src.interfaces.i_ig_selectors import IIGSelectors
from src.selectors.lite_instagram_app import LiteInstagramSelectors
from src.selectors.official_instagram_app import OfficialInstagramSelectors


class SelectorsFactory:
    def create_selectors(self, automation_app: str) -> IIGSelectors:
        if automation_app == 'official_instagram':
            return OfficialInstagramSelectors()
        elif automation_app == 'lite_instagram':
            return LiteInstagramSelectors()
        else:
            raise ValueError('Invalid automation app')
