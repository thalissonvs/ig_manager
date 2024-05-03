import uiautomator2 as u2

from src.interfaces.i_automator import IAutomator


class AndroidAutomator(IAutomator):
    def __init__(self, device_info: dict) -> None:
        self.device_info = device_info
        self.device_automator = u2.connect(self.device_info['device_id'])

    def click(self, element_selectors: dict, timeout=10) -> None:
        element = self.find_element(element_selectors)
        element.click(timeout=timeout)

    def send_keys(self, element_selectors: dict, keys: str) -> None:
        element = self.find_element(element_selectors)
        element.set_text(keys)

    def wait_for_element(self, element_selectors: dict, seconds: int) -> bool:
        element = self.find_element(element_selectors)
        return element.wait(timeout=seconds)

    def find_element(self, selectors: dict) -> u2.UiObject:
        element = self.device_automator(**selectors)
        return element
