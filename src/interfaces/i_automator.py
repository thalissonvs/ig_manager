from abc import ABC, abstractmethod


class IAutomator(ABC):
    @abstractmethod
    def click(self, element) -> None:
        pass

    @abstractmethod
    def send_keys(self, element, keys) -> None:
        pass

    @abstractmethod
    def wait_for_element(self, element, seconds) -> None:
        pass

    @abstractmethod
    def find_element(self, selectors) -> None:
        pass
