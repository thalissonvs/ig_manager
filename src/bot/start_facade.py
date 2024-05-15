from src.automators.android_automator import AndroidAutomator
from src.bot.bot import Bot
from src.gui.models.config_model import ConfigModel
from src.gui.models.devices_model import DevicesModel
from src.gui.models.groups_model import GroupsModel
from src.managers.instagram_manager import InstagramManager
from src.selectors.selectors_factory import SelectorsFactory


class StartBotFacade:
    def __init__(
        self,
        selectors_factory: SelectorsFactory,
        groups_model: GroupsModel,
        config_model: ConfigModel,
    ) -> None:
        self.selectors_factory = selectors_factory
        self.groups_model = groups_model
        self.config_model = config_model

    def start(
        self,
        group_index: int,
    ) -> None:
        group_model = self.groups_model.get_group_model(group_index)
        device_id = group_model.device_id
        automation_app = self.config_model.automation_app

        automator = AndroidAutomator(device_id, automation_app)

        selectors = self.selectors_factory.create_selectors(automation_app)
        instagram_manager = InstagramManager(automator, selectors)
        instagram_bot = Bot(instagram_manager, group_model, self.config_model)
        return instagram_bot.start()
