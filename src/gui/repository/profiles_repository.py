import json

DEFAULT_PATH = 'userdata/profiles.json'


class ProfilesRepository:
    def __init__(self, file_path: str = DEFAULT_PATH) -> None:
        self.file_path = file_path

    def set_profiles(self, options: dict) -> None:
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(options, file, indent=4)

    def get_profiles(self) -> dict:
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    
    def add_new_profile(self, profile: dict) -> None:
        profiles = self.get_profiles()
        profiles[profile['username']] = profile
        self.set_profiles(profiles)
    
    def remove_profile(self, username: str) -> None:
        profiles = self.get_profiles()
        profiles.pop(username)
        self.set_profiles(profiles)