import json
import os

from PyQt5.QtCore import QObject, pyqtSignal

from src.gui.constants import DEFAULT_OPTIONS
from src.gui.models.config_model import ConfigModel


class ConfigController(QObject):

    show_popup_signal = pyqtSignal(str, str)

    OPTIONS_PATH = os.path.join(os.getcwd(), 'userdata', 'options.json')

    def __init__(self, config_model: ConfigModel) -> None:
        super().__init__()
        self.config_model = config_model

    def set_options_if_valid(self) -> None:
        
        if not os.path.exists(self.OPTIONS_PATH):
            self._set_model_attr(DEFAULT_OPTIONS)
            return
        
        with open(self.OPTIONS_PATH, 'r') as f:
            options_content = f.read()

        try:
            options = json.loads(options_content)
        except json.JSONDecodeError:
            self._set_model_attr(DEFAULT_OPTIONS)
            return

        try:
            self._check_options_keys(options)
        except AttributeError:
            self._set_model_attr(DEFAULT_OPTIONS)
            return

        self.load_options(options)
        
    def load_options(self, options: dict) -> None:

        self._set_model_attr(options)

    def save_options(self, options: dict) -> None:

        self._set_model_attr(options)

        with open(self.OPTIONS_PATH, 'w') as f:
            f.write(json.dumps(options, indent=4))

        self.show_popup_signal.emit(
            'Sucesso!', 'Configurações salvas com sucesso!'
        )

    def _set_model_attr(self, options: dict) -> None:
        
        self._check_options_keys(options)
        
        for key, value in options.items():
            if key in DEFAULT_OPTIONS:
                setattr(self.config_model, key, value)
    
    def _check_options_keys(self, options: dict) -> None:
        if not set(options.keys()) == set(DEFAULT_OPTIONS.keys()):
            raise AttributeError('Invalid options keys')