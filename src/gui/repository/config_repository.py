import json

DEFAULT_PATH = 'userdata/options.json'

class ConfigRepository:
    def __init__(self, file_path: str = DEFAULT_PATH) -> None:
        self.file_path = file_path
    
    def set_options(self, options: dict) -> None:
        with open(self.file_path, 'w') as file:
            json.dump(options, file, indent=4)
    
    def get_options(self) -> dict:
        try:
            with open(self.file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
