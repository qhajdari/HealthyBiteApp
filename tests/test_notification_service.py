# app/services/notification_service.py
from abc import ABC, abstractmethod

class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str, target: str) -> str:
        """Send a notification and return the rendered message."""
        pass

class EmailNotification(NotificationService):
    def send_notification(self, message: str, target: str) -> str:
        rendered = f"Sending EMAIL to {target}: {message}"
        print(rendered)
        return rendered

class SMSNotification(NotificationService):
    def send_notification(self, message: str, target: str) -> str:
        rendered = f"Sending SMS to {target}: {message}"
        print(rendered)
        return rendered
