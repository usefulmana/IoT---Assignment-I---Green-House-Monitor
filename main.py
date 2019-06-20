import datetime
import os
from sense_hat import SenseHat
from database import Database

# def get_cpu_temp():
#   res = os.popen("vcgencmd measure_temp").readline()
#   t = float(res.replace("temp=","").replace("'C\n",""))
#   return(t)
#
# database = Database()
# database.save_daily_notification('OK')
# print(database.check_notification_status())
# sense = SenseHat()

str1 = 'OK. This is good'
str2 = 'fadsf'
print(str1.find(str2))
print(False)