import uiautomator2 as u2


class AndroidAutomator:
    def __init__(self, device_id: int, automation_app: str) -> None:
        self.device_id = device_id
        self.automation_app = automation_app
        self.device_automator = u2.connect(self.device_id)

    def prepare(self) -> int:
        packages_map = {
            'official_instagram': 'com.instagram.android',
            'lite_instagram': 'com.instagram.lite',
        }

        package_name = packages_map.get(self.automation_app, None)
        if package_name is None:
            raise ValueError(f'Invalid automation app: {self.automation_app}')
        self.device_automator.app_start(package_name, use_monkey=True)
        return self.device_automator.app_wait(package_name)

    def click(self, element_selectors: dict, timeout: int = 10) -> None:
        element = self.find_element(element_selectors)
        element.click(timeout=timeout)

    def send_keys(
        self, element_selectors: dict, keys: str, timeout: int = 10
    ) -> None:
        element = self.find_element(element_selectors)
        self.wait_for_element(element, timeout)
        element.set_text(keys)

    def wait_for_element(self, element: u2.UiObject, seconds: int) -> None:
        if not element.wait(timeout=seconds):
            raise TimeoutError(f'Element not found: {element.info}')

    def find_element(self, selectors: dict) -> u2.UiObject | u2.xpath.XPath:

        if 'xpath' in selectors.keys():
            element = self.device_automator.xpath(selectors['xpath'])
            return element

        element = self.device_automator(**selectors)
        return element
