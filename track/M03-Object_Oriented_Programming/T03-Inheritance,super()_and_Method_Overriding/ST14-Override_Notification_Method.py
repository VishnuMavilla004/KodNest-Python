class Notification:
    def send(self, message):
        print(f"General Notification: {message}")


class EmailNotification(Notification):
    # Override send()
    def send(self, message):
        print(f"Email Notification: {message}")


message = input().strip()

# Create both objects and call send()
Notify = Notification()
Notify.send(message)
ENotify = EmailNotification()
ENotify.send(message)
