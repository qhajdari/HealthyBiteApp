from abc import ABC, abstractmethod

# Interface / Abstract Class
class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message, recipient):
        pass


# Implementation 1
class EmailNotification(NotificationService):
    def send_notification(self, message, recipient):
        print(f"Sending EMAIL to {recipient}: {message}")


# Implementation 2
class SMSNotification(NotificationService):
    def send_notification(self, message, recipient):
        print(f"Sending SMS to {recipient}: {message}")

