import datetime
import os
from sense_hat import SenseHat

def get_cpu_temp():
  res = os.popen("vcgencmd measure_temp").readline()
  t = float(res.replace("temp=","").replace("'C\n",""))
  return(t)



sense = SenseHat()
t = sense.get_temperature_from_humidity()
t_corr = t - ((get_cpu_temp()-t)/1.3)

print(t_corr)