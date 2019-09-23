#! /usr/bin/python3
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt

now = QDate.currentDate()

print(now.toString(Qt.ISODate))
# 2018-04-01
print(now.toString(Qt.DefaultLocaleLongDate))
# zondag 1 april 2018

datetime = QDateTime.currentDateTime()

print(datetime.toString())
# zo apr. 1 00:00:00

time = QTime.currentTime()

print(time.toString(Qt.DefaultLocaleLongDate))
# 00:00:00 CEST
