from pushbullet import PushBullet
from pushbullet.errors import PushbulletError, InvalidKeyError, PushError


class Notification:

    _instance = None
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
            self._API_KEY = 'o.IcOB60dNl8mrBFHVI0AJtx68ZmSTCJIO'

    def push_notification(self, title, body):
        try:
            pb = PushBullet(self._API_KEY)
            push = pb.push_note(title, body)
        except (PushbulletError, InvalidKeyError, PushError) as e:
            print(e)