from abc import ABC, abstractmethod


class UnderMaintenanceException(Exception):
    pass

class NotificationSender(ABC):
    def __init__(self):
        self.is_under_maintenance = False

    @abstractmethod
    def send(self, message: str):
        pass

    @property
    def is_under_maintenance(self):
        return self.__is_under_maintenance

    @is_under_maintenance.setter
    def is_under_maintenance(self, value):
        self.__is_under_maintenance = value


class EmailSender(NotificationSender):
    def send(self, message: str):
        return f"Sending email with message: {message}"


class SMSSender(NotificationSender):
    def send(self, message: str):
        return f"Sending SMS with message: {message}"


class PushSender(NotificationSender):
    def send(self, message: str):
        return f"Sending Push notification with message: {message}"


class NotificationService:
    def __init__(self, sender: NotificationSender):
        self.sender = sender

    def notify(self, message: str):
        if self.sender.is_under_maintenance:
            print("This service is currently under maintenance.")
        else:
            result = self.sender.send(message)
            print(result)

email_sender = EmailSender()
sms_sender = SMSSender()
push_sender = PushSender()

push_sender.is_under_maintenance = True

email_service = NotificationService(email_sender)
sms_service = NotificationService(sms_sender)
push_service = NotificationService(push_sender)

email_service.notify('Hello via email!')
sms_service.notify('Hello via SMS!')
push_service.notify('Hello via Push!')