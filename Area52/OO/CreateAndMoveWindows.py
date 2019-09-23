import sys, time
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)
from PyQt5.QtGui import QFont

class Example(QWidget):
	def __init__(self, x, y, naam):
		super().__init__()
		self.initUI(x,y, naam)

	def initUI(self, x, y, naam):
		self.x = x
		self.y = y
		self.naam = naam
		self.setWindowTitle('Icon')
		self.setWindowIcon(QIcon('ICO.ico'))

		qbtn = QPushButton('Quit', self)
		qbtn2 = QPushButton('enter', self)
		qbtn.clicked.connect(QApplication.instance().quit)
		qbtn2.clicked.connect(self.new)
		qbtn.resize(qbtn.sizeHint())
		qbtn2.resize(qbtn2.sizeHint())
		qbtn.move(50,50)
		qbtn2.move(50,100)

		self.setGeometry(x,y,250, 150)
		self.setWindowTitle(naam)
		self.show()

	def new(self):
		print('New')



if __name__ == '__main__':
	app = QApplication(sys.argv)
	A = Example(600,500, 'A')
	time.sleep(.5)
	B = Example(300,300, 'B')
	time.sleep(.5)
	C = Example(600,300, 'C')
	time.sleep(.5)
	D = Example(900,300, 'D')
	time.sleep(.5)
	L = Example(300,500, 'L')
	time.sleep(.5)
	R = Example(900,500, 'R')
	time.sleep(.5)
	E = Example(300,700, 'E')
	time.sleep(.5)
	F = Example(600,700, 'F')
	time.sleep(.5)
	G = Example(900,700, 'G')

	sys.exit(app.exec_())