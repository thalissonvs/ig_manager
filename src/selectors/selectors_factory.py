from src.interfaces.i_selectors import ISelectors
from src.selectors.lite_instagram_selectors import LiteInstagramSelectors
from src.selectors.official_instagram_selectors import (
    OfficialInstagramSelectors,
)


class SelectorsFactory:
    def create_selectors(
        self, automation_platform: str, automation_app: str
    ) -> ISelectors:
        if automation_platform == 'android':
            if automation_app == 'official_instagram':
                return OfficialInstagramSelectors()
            elif automation_app == 'lite_instagram':
                return LiteInstagramSelectors()
            else:
                raise ValueError('Invalid automation app')
        else:
            raise ValueError('Invalid automation platform')
