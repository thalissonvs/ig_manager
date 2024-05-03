from src.automators.automator_factory import AutomatorFactory
from src.bot.instagram_bot import InstagramBot
from src.gui.models.config_model import ConfigModel
from src.gui.models.devices_model import DevicesModel
from src.gui.models.profiles_model import ProfilesModel
from src.instagram.instagram_manager import InstagramManager
from src.selectors.selectors_factory import SelectorsFactory


class InstagramBotFacade:
    def __init__(
        self,
        automator_factory: AutomatorFactory,
        selectors_factory: SelectorsFactory,
    ) -> None:
        self.automator_factory = automator_factory
        self.selectors_factory = selectors_factory

    def start(
        self,
        devices_model: DevicesModel,
        profiles_model: ProfilesModel,
        config_model: ConfigModel,
        profile_info: dict,
        device_id: str = None,
    ) -> None:
        device_info = (
            devices_model.get_device(device_id) if device_id else None
        )
        automation_platform = config_model.automation_platform
        automation_app = config_model.automation_app

        automator = self.automator_factory.create_automator(
            automation_platform, device_info
        )
        selectors = self.selectors_factory.create_selectors(
            automation_platform, automation_app
        )
        instagram_manager = InstagramManager(automator, selectors)
        instagram_bot = InstagramBot(
            instagram_manager, profiles_model, config_model
        )
        return instagram_bot.start(profile_info)
