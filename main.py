import sys

from PyQt5.QtWidgets import QApplication

from src.bot.start_facade import StartBotFacade
from src.gui.controllers.config_controller import ConfigController
from src.gui.controllers.devices_controller import DevicesController
from src.gui.controllers.profiles_controller import ProfilesController
from src.gui.controllers.start_controller import StartController
from src.gui.models.config_model import ConfigModel
from src.gui.models.devices_model import DevicesModel
from src.gui.models.profiles_model import ProfilesModel
from src.gui.repository.config_repository import ConfigRepository
from src.gui.repository.profiles_repository import ProfilesRepository
from src.gui.services.adb_service import ADBService
from src.gui.services.profiles_service import ProfilesService
from src.gui.views.add_profiles_view import AddProfilesView
from src.gui.views.edit_profile_view import EditProfileView
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
    profiles_model = ProfilesModel()
    profiles_repository = ProfilesRepository()
    profiles_controller = ProfilesController(
        profiles_model, ProfilesService(), profiles_repository
    )
    edit_profile_view = EditProfileView(profiles_controller)
    add_profiles_view = AddProfilesView(profiles_controller)

    selectors_factory = SelectorsFactory()
    bot_facade = StartBotFacade(selectors_factory)

    start_controller = StartController(
        devices_model, profiles_model, config_model, bot_facade
    )

    main_view = MainView(
        config_controller,
        devices_controller,
        profiles_controller,
        start_controller,
        add_profiles_view,
        edit_profile_view,
    )

    main_view.show()
    status = sys.exit(app.exec_())
