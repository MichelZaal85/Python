import sys
from PyQt5 import QtCore, QtGui, QtWidgets


def window():
   app = QtWidgets.QApplication(sys.argv)
   Dialog = QtWidgets.QDialog()
   win = QtWidgets.QDialog()

   b1 = QtWidgets.QPushButton(win)
   b1.setText("Button1")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)

   b2 = QtWidgets.QPushButton(win)
   b2.setText("Button2")
   b2.move(50,50)
   b2.clicked.connect(b2_clicked)

   win.setGeometry(100,100,200,100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
   print("Button 1 clicked")

def b2_clicked():
   print("Button 2 clicked")

if __name__ == '__main__':
   window()
