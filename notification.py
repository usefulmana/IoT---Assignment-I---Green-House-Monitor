from pushbullet import PushBullet
from pushbullet.errors import PushbulletError, InvalidKeyError, PushError
from json_parser import Parser


class Notification:
    """This class stores the method to send notification via PushBullet API"""
    _instance = None
    # Only one instance of this class should exist
    @staticmethod
    def get_instance():
        if Notification._instance is None:
            Notification()
        return Notification._instance

    def __init__(self):
        if Notification._instance is not None:
            raise Exception("This is a singleton class")
        else:
            Notification._instance = self
            self._API_KEY = Parser.get_instance().api_key

    def push_notification(self, title, body):
        try:
            pb = PushBullet(self._API_KEY)
            push = pb.push_note(title, body)
        except (PushbulletError, InvalidKeyError, PushError) as e:
            print(e)