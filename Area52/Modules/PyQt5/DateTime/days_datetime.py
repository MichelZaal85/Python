#! /usr/bin/python3

from PyQt5.QtCore import QDate

now = QDate.currentDate()

d = QDate(1945, 5, 5)

print("Days in month: {0}".format(d.daysInMonth()))
print("Days in year: {0}".format(d.daysInYear()))
