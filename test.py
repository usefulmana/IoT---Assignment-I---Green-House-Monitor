# from database import Database
# from createReport import Report
# from json_parser import Parser
#
# parser = Parser()
# db = Database()
# # print(db.get_all_dates_from_database(parser.number_of_days_in_report))
# print('fdasf')
# print(db.read_today_data())

# for i in a:
#     for j in i:
#         print(j[0], end=' ')
#     print('')
#     print('a')
#
# for i in a:
#     print(i)

import subprocess as sp
import os

# To pair devices see: https://www.cnet.com/how-to/how-to-setup-bluetooth-on-a-raspberry-pi-3/
# sudo apt install bluetooth bluez blueman
# pip3 install pybluez
#
# To use bt-device: sudo apt install bluez-tools

# Get list of paired devices.
# p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
# (stdout, stdin) = (p.stdout, p.stdin)
#
# data = stdout.readlines()
# print(data)
from sense_hat import SenseHat
import time

sense = SenseHat()
temp1 = sense.get_temperature_from_humidity()
print("Temperature: %s C" % temp1)

temp2 = sense.get_temperature_from_pressure()
print("Temperature: %s C" % temp2)

pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

# Alternatives.
print(sense.pressure)

# IMU sensors.
orientation = sense.get_orientation_degrees()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

orientation = sense.get_orientation()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**orientation))

# Alternatives.
print(sense.orientation)

north = sense.get_compass()
print("North: %s" % north)

# Alternatives.
print(sense.compass)

# Gyroscope.
gyro_only = sense.get_gyroscope()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**gyro_only))

# Alternatives.
print(sense.gyro)
print(sense.gyroscope)

# Accelerometer.
accel_only = sense.get_accelerometer()
print("p: {pitch}, r: {roll}, y: {yaw}".format(**accel_only))

# Alternatives.
print(sense.accel)
print(sense.accelerometer)

