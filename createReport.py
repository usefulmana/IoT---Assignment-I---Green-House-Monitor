import csv
import datetime
from database import Database


class Report:
    @staticmethod
    def create_report(data):
        """ Creating or overwriting the report.csv file """
        with open("report.csv", "w+") as report:
            writer = csv.writer(report)
            writer.writerow(["Date", "Status"])
            for d in data:
                writer.writerow([d[1].strftime("%Y-%m-%d"), d[2]])
            report.close()

    @staticmethod
    def chunks(l, n):
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def create_detailed_report():
        db = Database()

        with open("detailed_data.csv", "w+") as report:
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
    def create_daily_report():
        db = Database()
        with open('daily_report.csv', 'w+') as report:
            writer = csv.writer(report)
            writer.writerow(["date", "temperature", "humidity"])
            data = db.read_today_data()
            for i in data:
                writer.writerow([i[1], i[2], i[3]])
            report.close()


database = Database()
Report.create_report(database.read_daily_notification())
Report.create_detailed_report()
Report.create_daily_report()