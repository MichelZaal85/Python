# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressBar.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
i = 0
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(110, 100, 118, 23))
        self.progressBar.setProperty("value", i)
        self.progressBar.setObjectName("progressBar")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

    def increment(self):
        A = ['a','b','b','b','e','e','c','c','c','c'] # 4
        B = ['a','b','c','c','c','c','e'] #25
        C = ['a','b','c','d','e','c','e','e'] # 10
        D = ['a','b','c','d','e','e','e','e','e'] # 5

        import time
        i = 0
        maxLength = len(A) + len(A) * len(B) + len(A) * len(C) + len(A) * len(C) * len(D)
        incrementer = 100 / maxLength
        for x in A:
            i += incrementer
            # printProgressBar(i, 100)
            time.sleep(0.01)
            for y in B:
                i += incrementer
                # printProgressBar(i, 100)
                time.sleep(0.01)
            for z in C:
                i += incrementer
                # printProgressBar(i, 100)
                time.sleep(0.01)
                for a in D:
                    i += incrementer
                    # printProgressBar(i, 100)
                    time.sleep(0.01)
        i = 100
        return i



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    ui.increment()
    sys.exit(app.exec_())

    