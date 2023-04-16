from abc import ABC, abstractmethod


class SmartPhone(ABC):
    mobileName = "One +"

    @abstractmethod
    def camera(self):
        pass

    @abstractmethod
    def mediaplayer(self):
        pass

    @abstractmethod
    def whatsapp(self):
        pass

    @abstractmethod
    def youtube(self):
        print("coming soon")

    @abstractmethod
    def weatherapp(self):
        print("today the weather is cloudy")


class Phone(SmartPhone):

    def __init__(self, contacts, message, notes):
        self.contacts = contacts
        self.message = message
        self.notes = notes

    def camera(self):
        print("On the camera")

    def mediaplayer(self):
        print("Play Music")

    def whatsapp(self):
        print("send Message")

    def weatherapp(self):
        return super().weatherapp()

    def youtube(self):
        return super().youtube()


obj1 = Phone("Anaya", "send message to ria", "full stact")
obj1.camera()
obj1.mediaplayer()
obj1.whatsapp()
obj1.weatherapp()
obj1.youtube()
