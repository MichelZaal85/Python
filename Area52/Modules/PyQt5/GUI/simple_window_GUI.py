#! /usr/bin/python3
# -*- coding: utf-8 -*-

'''
Simple PyQt5 window
'''

import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Every PyQt5 application must create an application object.
    # The sys.argv parameter is a list of arguments from a command line.
    # Python scripts can be run from the shell. It is a way how we can
    # control the startup of our scripts.

    w = QWidget()
    # The QWidget widget is the base class of all user interface objects
    # in PyQt5. We provide the default constructor for QWidget.
    # The default constructor has no parent. A widget with no parent is
    # called a window.

    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple Window')
    w.show()

    sys.exit(app.exec_())
    # exec is a Python keyword, so exec_() was created.
