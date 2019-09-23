#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        qbtn = QPushButton('Quit', self)
        # The first parameter is the label, second the parent widget

        qbtn.clicked.connect(QApplication.instance().quit)
        '''
        The event processing system in PyQt5 is built with the
        signal & slot mechanism. If we click on the button, the
        signal clicked is emitted. The slot can be a Qt slot or
        any Python callable.
        the sender signal (btn) is recieved by the receiver (app)
        '''

        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
