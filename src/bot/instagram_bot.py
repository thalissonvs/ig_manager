"""
Essa é a main do bot, onde o bot é instanciado, a factory do instagram_manager é instanciada,
o instagram_manager é instanciado e o bot é iniciado. Dessa forma, para adicionar um novo
instagram_manager, basta criar uma nova classe que implemente a interface IInstagramManager
e adicionar na factory. Irá receber uma instância dos models para poder alterar o estado
da aplicação e refletir na interface gráfica.
"""
from src.gui.models.config_model import ConfigModel
from src.gui.models.profiles_model import ProfilesModel
from src.instagram.instagram_manager import InstagramManager


class InstagramBot:
    def __init__(
        self,
        instagram_manager: InstagramManager,
        profiles_model: ProfilesModel,
        config_model: ConfigModel,
    ) -> None:
        self.instagram_manager = instagram_manager
        self.config_model = config_model
        self.profiles_model = profiles_model

    def start(self, profile_info: dict):
        print('Bot started with profile:', profile_info)
