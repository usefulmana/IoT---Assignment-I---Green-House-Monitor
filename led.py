from sense_hat import SenseHat


class LED:

    def __init__(self):
        self._red_led = (255, 0, 0)
        self._green_led = (0, 255, 0)
        self.sense = SenseHat()

    def red_light_on(self):
        self.sense.clear(self._red_led)

    def green_light_on(self):
        self.sense.clear(self._green_led)