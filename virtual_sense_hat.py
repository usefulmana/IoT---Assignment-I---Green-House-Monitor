import logging
try:
    from sense_hat import SenseHat
except ImportError:
    pass


class VirtualSenseHat:
    """Added a duck type class in case the RPi or sense hat breaks down"""
    @staticmethod
    def getSenseHat(logError = True):
        try:
            return SenseHat()
        except Exception as e:
            if(logError):
                logging.error("Falling back to VirtualSenseHat because: " + str(e))
            return VirtualSenseHat()

    def __init__(self):
        self.default_temp = 0
        self.default_humidity = 0

    def get_temperature(self):
        return self.default_temp

    def get_humidity(self):
        return self.default_humidity

    def show_message(self, text_string,
        scroll_speed = 0.1, text_colour = [255, 255, 255], back_colour = [0, 0, 0]):
        print(text_string)

    def clear(self):
        pass
