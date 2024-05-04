from src.automators.android_automator import AndroidAutomator
from src.bot.bot import Bot
from src.gui.models.config_model import ConfigModel
from src.gui.models.devices_model import DevicesModel
from src.gui.models.profiles_model import ProfilesModel
from src.managers.instagram_manager import InstagramManager
from src.selectors.selectors_factory import SelectorsFactory


class StartBotFacade:
    def __init__(
        self,
        selectors_factory: SelectorsFactory,
    ) -> None:
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
        automation_app = config_model.automation_app if device_info else None

        automator = AndroidAutomator(device_info, automation_app)

        selectors = self.selectors_factory.create_selectors(
            automation_app
        )
        instagram_manager = InstagramManager(automator, selectors)
        instagram_bot = Bot(instagram_manager, profiles_model, config_model)
        return instagram_bot.start(profile_info)
