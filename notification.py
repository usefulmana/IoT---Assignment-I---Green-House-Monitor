from pushbullet import PushBullet
from pushbullet.errors import PushbulletError, InvalidKeyError, PushError


class Notification:
    def __init__(self):
        self._API_KEY = 'o.IcOB60dNl8mrBFHVI0AJtx68ZmSTCJIO'

    def push_notification(self, title, body):
        try:
            pb = PushBullet(self._API_KEY)
            push = pb.push_note(title, body)
        except (PushbulletError, InvalidKeyError, PushError) as e:
            print(e)