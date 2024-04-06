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

    def set_default_options(self) -> None:
        for key, value in DEFAULT_OPTIONS.items():
            setattr(self.config_model, key, value)

    def set_options_if_valid(self) -> None:
        options_content = (
            open(self.OPTIONS_PATH, 'r').read()
            if os.path.exists(self.OPTIONS_PATH)
            else ''
        )

        try:
            options = json.loads(options_content)
        except json.JSONDecodeError:
            self.set_default_options()
            return

        if not set(options.keys()) == set(DEFAULT_OPTIONS.keys()):
            self.set_default_options()
            return

        self.load_options(options)

    def load_options(self, options: dict) -> None:

        if not set(options.keys()) == set(DEFAULT_OPTIONS.keys()):
            raise AttributeError('Invalid options keys')

        for key, value in options.items():
            if key in DEFAULT_OPTIONS:
                setattr(self.config_model, key, value)

    def save_options(self, options: dict) -> None:

        if not set(options.keys()) == set(DEFAULT_OPTIONS.keys()):
            raise AttributeError('Invalid options keys')

        for key, value in options.items():
            if key in DEFAULT_OPTIONS:
                setattr(self.config_model, key, value)

        with open(self.OPTIONS_PATH, 'w') as f:
            f.write(json.dumps(options, indent=4))

        self.show_popup_signal.emit(
            'Sucesso!', 'Configurações salvas com sucesso!'
        )
