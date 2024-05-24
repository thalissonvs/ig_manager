from abc import ABC, abstractmethod


class IManager(ABC):
    @abstractmethod
    def prepare(self) -> None:
        pass

    @abstractmethod
    def login(self, username: str, password: str) -> bool:
        pass

    @abstractmethod
    def logout(self) -> bool:
        pass

    @abstractmethod
    def add_new_account(self) -> None:
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

    @abstractmethod
    def is_no_account_logged(self) -> bool:
        pass

    @abstractmethod
    def get_logged_accounts(self) -> list:
        pass

    @abstractmethod
    def change_to_account(self, username: str) -> bool:
        pass
