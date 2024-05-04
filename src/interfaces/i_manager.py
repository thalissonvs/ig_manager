from abc import ABC, abstractmethod


class IManager(ABC):
    @abstractmethod
    def login(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def follow(self, username: str) -> bool:
        pass

    @abstractmethod
    def like(self, url: str) -> bool:
        pass

    @abstractmethod
    def comment(self, url: str, comment: str) -> bool:
        pass
