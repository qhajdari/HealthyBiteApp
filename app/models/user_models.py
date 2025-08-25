from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username: str):
        self._username = None
        self.username = username  # kjo kalon te setter per validim

    @property
    def username(self) -> str:
        return self._username

    @username.setter
    def username(self, value: str) -> None:
        if not value or len(value) < 3:
            raise ValueError("Username must have at least 3 characters")
        self._username = value

    @abstractmethod
    def get_role(self) -> str:
        """Return the role name ('Regular', 'Premium', 'Admin')."""
        pass


class RegularUser(User):
    def get_role(self) -> str:
        return "Regular"


class PremiumUser(RegularUser):
    def get_role(self) -> str:
        return "Premium"


class AdminUser(User):
    def get_role(self) -> str:
        return "Admin"
