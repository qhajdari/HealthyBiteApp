import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.notification_service import EmailNotification, SMSNotification

if __name__ == "__main__":
    email = EmailNotification()
    sms = SMSNotification()

    email.send_notification("New meal plan is ready", "qh43141@ubt-uni.net")
    sms.send_notification("Do not forget to eat breakfast", "+38349908800")
