#! /usr/bin/python3
from PyQt5.QtCore import QDateTime, Qt

now = QDateTime.currentDateTime()

print("\nUTC (Universal Coordinated Time\n")

now = QDateTime.currentDateTime()

print("Locale datetime:", now.toString(Qt.ISODate))
print("Universal datetime:", now.toUTC().toString(Qt.ISODate))

print("The offset from UTC is: {} seconds".format(now.offsetFromUtc()))
