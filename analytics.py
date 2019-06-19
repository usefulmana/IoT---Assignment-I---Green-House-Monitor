import csv
from database import Database


class Report:

    @staticmethod
    def create_csv(message):
        with open('report.csv', 'w+') as report:
            writer = csv.writer(report)
            writer.writerow(['Date', 'Status'])
            for i in message:
                writer.writerow(i[0], i[1])
