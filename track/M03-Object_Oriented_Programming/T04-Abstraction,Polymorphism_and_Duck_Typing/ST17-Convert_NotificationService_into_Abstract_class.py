from abc import ABC, abstractmethod


class NotificationService(ABC):
    # Add abstract notify()
    @abstractmethod
    def notify(self):
        pass


class EmailNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def send_email(self):
        return f"Email: {self.message}"

    # Implement notify()
    def notify(self):
        return f"Email: {self.message}"


class SMSNotificationService(NotificationService):
    def __init__(self, message):
        self.message = message

    def send_sms(self):
        return f"SMS: {self.message}"

    # Implement notify()
    def notify(self):
        return f"SMS: {self.message}"


message = input()

# Create both objects and call notify()
email = EmailNotificationService(message)
sms = SMSNotificationService(message)

Service = [email, sms]

for notification in Service:
    print(notification.notify())