from database import Database
from createReport import Report
from json_parser import Parser

parser = Parser()
db = Database()
# print(db.get_all_dates_from_database(parser.number_of_days_in_report))
print('fdasf')
print(db.read_today_data())

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
