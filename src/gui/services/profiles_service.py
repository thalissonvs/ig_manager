class ProfilesService:
    @staticmethod
    def format_profiles_text(profiles_text: str) -> list[dict]:
        profiles = []
        for profile in profiles_text.split('\n'):
            if profile:
                username, password, gender = profile.split(' ')
                profiles.append(
                    {
                        'username': username,
                        'password': password,
                        'gender': gender,
                    }
                )
        return profiles
