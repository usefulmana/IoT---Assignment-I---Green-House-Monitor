import time
import sqlite3
from sense_hat import SenseHat

delay_seconds = 60

# =====================================================
# Get data from Sense HAT
# =====================================================


def get_data_from_sensors():
    # Retrieve data from sensors
    sense = SenseHat()
    temperature = sense.get_temperature()
    humidity = sense.get_humidity()

    # Round up values if not null
    if temperature is None:
        temperature = 0
    else:
        temperature = round(temperature, 1)

    if humidity is None:
        humidity = 0
    else:
        humidity = round(humidity, 1)

    # Return temperature and humidity values
    return [temperature, humidity]


# =====================================================
# Log data on database
# =====================================================


def log_data(temperature, humidity):
    db = sqlite3.connect('greenhouse.db')
    db_cursor = db.cursor()
    values = "datetime('now'), {}, {}".format(temperature, humidity)
    db_cursor.execute('insert into GREENHOUSE_DATA values({})'.format(values))
    db.commit()
    db.close()


# =====================================================
# Main function
# =====================================================


def main():
    while 1:
        print('Getting data...', end=' ')
        [temperature, humidity] = get_data_from_sensors()
        log_data(temperature=temperature, humidity=humidity)
        print('Temperature: {} - Humidity: {}'.format(temperature, humidity))
        print('Sleeping.\n')
        time.sleep(delay_seconds)

main()
