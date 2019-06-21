import csv
from database import Database


class Report:
    @staticmethod
    def create_report(data):
        """ Creating or overwriting the report.csv file """
        with open("report.csv", "a") as report:
            writer = csv.writer(report)
            writer.writerow(["Date", "Status"])
            for d in data:
                writer.writerow([d[1].strftime("%Y-%m-%d"), d[2]])
            report.close()


database = Database()
Report.create_report(database.read_daily_notification())