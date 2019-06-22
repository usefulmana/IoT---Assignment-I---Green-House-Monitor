import csv
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
            writer.writerow(["Date", "Avg. Temperature", "Avg. Humidity", "Min Temp", "Max Temp", "Min Humid", "Max Humid"])
            data = list(Report.chunks(db.get_detailed_daily_report(), 7))
            for i in data:
                writer.writerow([i[0][0].strftime("%Y-%m-%d"), i[1][0], i[2][0], i[3][0], i[4][0], i[5][0], i[6][0]])
            report.close()


database = Database()
Report.create_report(database.read_daily_notification())
Report.create_detailed_report()
