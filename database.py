import sqlite3

con = sqlite3.connect('greenhouse.db')
with con:
    cur = con.cursor()
    cur.execute('drop table if exists GREENHOUSE_DATA')
    cur.execute('create table GREENHOUSE_DATA('
                'time_stamp datetime, '
                'temperature numeric, '
                'humidity numeric)')

