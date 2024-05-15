"""
Essa é a main do bot, onde o bot é instanciado, a factory do instagram_manager é instanciada,
o instagram_manager é instanciado e o bot é iniciado. Dessa forma, para adicionar um novo
instagram_manager, basta criar uma nova classe que implemente a interface IInstagramManager
e adicionar na factory. Irá receber uma instância dos models para poder alterar o estado
da aplicação e refletir na interface gráfica.
"""
from src.gui.models.config_model import ConfigModel
from src.gui.models.groups_model import GroupModel
from src.interfaces.i_manager import IManager


class Bot:
    def __init__(
        self,
        manager: IManager,
        group_model: GroupModel,
        config_model: ConfigModel,
    ) -> None:
        self.manager = manager
        self.config_model = config_model
        self.group_model = group_model

    def start(self) -> None:
        print('Bot started')
