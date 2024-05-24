from src.automators.android_automator import AndroidAutomator
from src.bot.bot import Bot
from src.clients.actions_client import ActionsClient
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
        device_id = self.groups_model.get_group_info(group_index)['device_id']
        automation_app = self.config_model.automation_app

        automator = AndroidAutomator(device_id)

        selectors = self.selectors_factory.create_selectors(automation_app)
        instagram_manager = InstagramManager(automator, selectors)
        actions_client = ActionsClient()
        instagram_bot = Bot(
            instagram_manager,
            self.groups_model,
            self.config_model,
            actions_client,
            group_index,
        )
        return instagram_bot.start()
