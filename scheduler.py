from crontab import CronTab

pi_cron = CronTab(user='pi')
pi_cron.remove_all()


test_job = pi_cron.new(command="python -u /home/pi/Desktop/IoT/test.py")
test_job.minute.every(1)
# schedule_monitor = pi_cron.new(command="/usr/bin/python3.5 -u /home/pi/Desktop/IoT/monitorAndNotify.py")
# schedule_monitor.minute.every(1)
#
# schedule_bluetooth = pi_cron.new(command="/usr/bin/python3.5 -u /home/pi/Desktop/IoT/bluetooth_messenger.py")
# schedule_bluetooth.minute.every(1)
#
# schedule_report = pi_cron.new(command="/usr/bin/python3.5 -u /home/pi/Desktop/IoT/createReport.py")
# schedule_bluetooth.hour.every(1)

for item in pi_cron:
    print(item)

pi_cron.write()