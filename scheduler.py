from crontab import CronTab


class Scheduler:
    """ This class is responsible for adding the below scripts into RPi's crontab"""
    @staticmethod
    def run_script():
        pi_cron = CronTab(user='pi')
        pi_cron.remove_all()

        # Schedule the monitor app to run every minute
        schedule_monitor = pi_cron.new(command="cd /home/pi/Desktop/IoT && /usr/bin/python3.5 monitorAndNotify.py")
        schedule_monitor.minute.every(1)

        # Schedule bluetooth app to run every minute
        schedule_bluetooth = pi_cron.new(command="cd /home/pi/Desktop/IoT && /usr/bin/python3.5 bluetooth_messenger.py")
        schedule_bluetooth.minute.every(5)

        # Schedule to create a report every 3 hours
        schedule_report = pi_cron.new(command="cd /home/pi/Desktop/IoT && /usr/bin/python3.5 createReport.py")
        schedule_report.hour.every(3)

        pi_cron.write()


Scheduler.run_script()

