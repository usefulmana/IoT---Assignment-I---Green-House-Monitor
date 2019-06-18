from sense_hat import SenseHat

sense = SenseHat()
red = (255, 0, 0)
sense.clear()

temperature = sense.get_temperature_from_pressure()
humidity = sense.get_humidity()
print(temperature,    humidity)
