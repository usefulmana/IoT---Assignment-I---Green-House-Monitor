from datetime import datetime
myFile = open('append.txt', 'w+')
myFile.write('\nAccessed on ' + str(datetime.now()))