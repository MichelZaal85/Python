#! /usr/bin/python3

from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()

print("Gregorian date for today: ", now.toString(Qt.ISODate))
print("Julian day (JDN) for today: ", now.toJulianDay())
print("Julian day number since 01-01-4713 BC.")
