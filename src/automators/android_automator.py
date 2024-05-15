import uiautomator2 as u2
from time import sleep
import threading


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

    def find_element(self, selectors: list[dict], timeout: int = 5) -> u2.UiObject | u2.xpath.XPath:
        found_element = None
        found_condition = threading.Condition()

        def _find_element(selector, timeout) -> None:
            nonlocal found_element
            if 'xpath' in selector:
                _find_by_xpath(selector['xpath'], timeout)
            else:
                _find_by_selector(selector, timeout)
        
        def _find_by_xpath(xpath, timeout) -> None:
            nonlocal found_element
            element = self.device_automator.xpath(xpath)
            if element.wait(timeout=timeout):
                _notify_found_element(element)
        
        def _find_by_selector(selector, timeout) -> None:
            nonlocal found_element
            element = self.device_automator(**selector)
            if element.wait(timeout=timeout):
                _notify_found_element(element)
        
        def _notify_found_element(element) -> None:
            nonlocal found_element
            with found_condition:
                if found_element is None:
                    found_element = element
                    found_condition.notify_all()
        
        threads = [threading.Thread(target=_find_element, args=(selector, timeout)) for selector in selectors]
        for thread in threads:
            thread.start()
        
        with found_condition:
            found_condition.wait(timeout)
        
        for thread in threads:
            thread.join(0.1)
        
        return found_element