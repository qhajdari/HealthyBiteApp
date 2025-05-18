# models/user_models.py
from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def get_role(self):
        pass


class RegularUser(User):
    def get_role(self):
        return "Regular"


class PremiumUser(RegularUser):
    def get_role(self):
        return "Premium"


class AdminUser(User):
    def get_role(self):
        return "Admin"
