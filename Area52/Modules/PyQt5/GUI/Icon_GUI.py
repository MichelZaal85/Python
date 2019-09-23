#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
This example shows an icon
in the titlebar of the window.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class Example(QWidget):

    def __init__(self):
        # The first __init__() is for the Example class

        super().__init__()
        # The super() method returns the parent object of the example class
        # the second constructor is for the inherited class

        self.initUI()
        # The creation of the GUI is delegated to the initUI() method.

    def initUI(self):

        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('\..\Resources\ICO.ico'))

        self.show()

        # All three methods have been inherited from the QWidget class.


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
