import json
import os

from PyQt5.QtCore import QObject, pyqtSignal

from src.gui.constants import DEFAULT_OPTIONS
from src.gui.models.config_model import ConfigModel
from src.gui.repository.config_repository import ConfigRepository


class ConfigController(QObject):

    config_changed = pyqtSignal(dict)

    def __init__(
        self, config_model: ConfigModel, config_repository: ConfigRepository
    ) -> None:
        super().__init__()
        self.config_model = config_model
        self.config_repository = config_repository
        self.config_model.config_changed.connect(self._emit_config_changed)

    def _emit_config_changed(self, config: dict) -> None:
        self.config_changed.emit(config)

    def _set_options_to_model(self, options: dict) -> None:
        for key, value in options.items():
            setattr(self.config_model, key, value)

    def _set_options_to_repository(self, options: dict) -> None:
        self.config_repository.set_options(options)

    def _get_options_from_repository(self) -> dict:
        return self.config_repository.get_options()

    def save_options(self, options: dict) -> None:
        """
        Método executado quando o usuário salva as opções.
        A view chama esse método passando um dicionário com as opções.
        Esse método então seta as opções no model e no repositório,
        assim também persistindo as opções no arquivo de configuração.
        """
        self._set_options_to_model(options)
        self._set_options_to_repository(options)

    def set_initial_options(self) -> None:
        """
        Método responsável por setar as opções iniciais do programa.
        Ele utiliza o repositório para buscar as opções salvas e aplica no model.
        O model por sua vez, ao ser atualizado, emite um sinal que é capturado pela view.
        E então a view atualiza os campos com os valores do model.
        """
        options = self._get_options_from_repository() or DEFAULT_OPTIONS
        self._set_options_to_model(options)
