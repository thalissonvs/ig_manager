from src.automators.android_automator import AndroidAutomator
from src.interfaces.i_automator import IAutomator


class AutomatorFactory:
    @staticmethod
    def create_automator(
        automator_platform: str, device_info: dict = None
    ) -> IAutomator:
        if automator_platform == 'android':
            if device_info is None:
                raise ValueError(
                    'Device info is required for Android automator'
                )
            return AndroidAutomator(device_info)

        raise ValueError(f'Invalid automator type: {automator_platform}')
