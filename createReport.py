import csv
import datetime
from database import Database
import time

class Report:
    """This class is responsible for creating daily, weekly and status reports"""
    @staticmethod
    def create_report(filename, data):
        """ Creating or overwriting the report.csv file """
        with open(filename, "w+") as report:
            writer = csv.writer(report)
            writer.writerow(["Date", "Status"])
            for d in data:
                writer.writerow([d[1].strftime("%Y-%m-%d"), d[2]])
            report.close()

    @staticmethod
    def chunks(l, n):
        """Split an array into even small arrays. Generator methods."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def create_detailed_report(filename):
        """This report will be used for task 2"""
        db = Database.get_instance()
        with open(filename, "w+") as report:
            writer = csv.writer(report)
            writer.writerow(
                ["date", "avg_temp", "avg_humid", "min_temp", "max_temp", "min_humid", "max_humid",
                 "created_on"])
            data = list(Report.chunks(db.get_detailed_daily_report(), 7))
            for i in data:
                writer.writerow([i[0][0].strftime("%Y-%m-%d"), i[1][0], i[2][0], i[3][0], i[4][0], i[5][0], i[6][0],
                                 datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
            report.close()

    @staticmethod
    def create_daily_report(filename):
        db = Database.get_instance()
        with open(filename, 'w+') as report:
            writer = csv.writer(report)
            writer.writerow(["date", "temperature", "humidity"])
            data = db.read_today_data()
            for i in data:
                writer.writerow([i[1], i[2], i[3]])
            report.close()


if __name__ == '__main__':
    time.sleep(10)
    database = Database.get_instance()
    Report.create_report("report.csv", database.read_daily_notification())
    Report.create_detailed_report("detailed_data.csv")
    Report.create_daily_report('daily_report.csv')