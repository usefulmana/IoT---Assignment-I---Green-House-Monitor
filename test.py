from database import Database
from createReport import Report
from json_parser import Parser

parser = Parser()
db = Database()
# print(db.get_all_dates_from_database(parser.number_of_days_in_report))
a = list(Report.chunks(db.get_detailed_daily_report(), 7))

# for i in a:
#     for j in i:
#         print(j[0], end=' ')
#     print('')
#     print('a')

# for i in a:
#     print(i)