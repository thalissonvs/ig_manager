import json

DEFAULT_PATH = 'userdata/profiles.json'


class GroupsRepository:
    def __init__(self, file_path: str = DEFAULT_PATH) -> None:
        self.file_path = file_path

    def set_groups(self, options: dict) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(options, file, indent=4)

    def get_groups(self) -> list:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
