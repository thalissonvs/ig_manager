import sys

from PyQt5.QtWidgets import QApplication

from src.bot.start_facade import StartBotFacade
from src.gui.controllers.config_controller import ConfigController
from src.gui.controllers.devices_controller import DevicesController
from src.gui.controllers.groups_controller import GroupsController
from src.gui.controllers.start_controller import StartController
from src.gui.models.config_model import ConfigModel
from src.gui.models.devices_model import DevicesModel
from src.gui.models.groups_model import GroupsModel
from src.gui.repository.config_repository import ConfigRepository
from src.gui.repository.groups_repository import GroupsRepository
from src.gui.services.adb_service import ADBService
from src.gui.views.add_profiles_view import AddProfilesView
from src.gui.views.main_view import MainView
from src.selectors.selectors_factory import SelectorsFactory

if __name__ == '__main__':
    app = QApplication(sys.argv)
    config_model = ConfigModel()
    config_repository = ConfigRepository()
    config_controller = ConfigController(config_model, config_repository)
    devices_model = DevicesModel()
    adb_service = ADBService('userdata\\platform-tools\\adb.exe')
    devices_controller = DevicesController(devices_model, adb_service)
    groups_model = GroupsModel()
    groups_repository = GroupsRepository()
    groups_controller = GroupsController(groups_model, groups_repository)
    selectors_factory = SelectorsFactory()
    start_bot_facade = StartBotFacade(
        selectors_factory, groups_model, config_model
    )
    start_controller = StartController(
        start_bot_facade,
    )
    add_profiles_view = AddProfilesView(groups_controller)
    main_view = MainView(
        config_controller,
        devices_controller,
        groups_controller,
        start_controller,
        add_profiles_view,
    )
    main_view.show()
    status = sys.exit(app.exec_())
