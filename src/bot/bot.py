"""
Essa é a main do bot, onde o bot é instanciado, a factory do instagram_manager é instanciada,
o instagram_manager é instanciado e o bot é iniciado. Dessa forma, para adicionar um novo
instagram_manager, basta criar uma nova classe que implemente a interface IInstagramManager
e adicionar na factory. Irá receber uma instância dos models para poder alterar o estado
da aplicação e refletir na interface gráfica.
"""
from src.gui.models.config_model import ConfigModel
from src.gui.models.profiles_model import ProfilesModel
from src.interfaces.i_manager import IManager


class Bot:
    def __init__(
        self,
        manager: IManager,
        profiles_model: ProfilesModel,
        config_model: ConfigModel,
    ) -> None:
        self.manager = manager
        self.config_model = config_model
        self.profiles_model = profiles_model

    def start(self, profile_info: dict) -> None:
        username = profile_info['username']
        self.profiles_model.update_profile_log(username, 'Realizando login...')
        status = self.manager.login(profile_info['username'], profile_info['password'])
        if status:
            self.profiles_model.update_profile_log(username, 'Login realizado com sucesso.')
        else:
            self.profiles_model.update_profile_log(username, 'Erro ao realizar login.')
            return
