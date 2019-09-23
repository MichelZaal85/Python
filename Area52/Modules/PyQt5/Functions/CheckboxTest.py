from PyQt5.QtWidgets import *
import sys, time
Locate = []
B_disc = []
X_disc = []
X_kind = []

L_Code = {'AP': "Academieplein",'BL': "Blaak",'DD': "RDM Droogdok",'ID': "RDM Innovation Dock",'KD': "Karel Doormanhof",'KZ': "Kralingse Zoom",'ME': "Max Eeuwelaan",'MP': "Museumpark",'MPL': "Museumpark",'MPH': "Museumpark",'PH': "Pieter De Hoochweg",'RS': "Rochussenstraat",'WD': "Wijnhaven 103",'WH': "Wijnhaven 61",'WN': "Wijnhaven 99",'WZ': "Wijhaven 107",'ZB': "Zorgboulevard"}
B_Code = {'B1': "Plattegrond",'B2': "Constructie",'B3': "Gevelaanzicht",'B4': "Doorsneden",'B5': "Detail"}
X_Code = {'E': "Elektrotechnische installatie",'W': "Werktuigbouwkundige installatie",'D': "Data installatie",'F': "Brandmeldinstallatie",'A': "Bliksem en Aardinginstallatie",'G': "Veiligheidsplattegrond",'Q': "Beveiligingsinstallatie",'S': "Sprinkler"}
X_Kind = {'1': "Plattegrond",'2': "Blokschema",'3': "Principeschema",'4': "Installatieschema",'5': "Detail",'6': "Stuurstroom",'7': "Aanzicht",'8': "Groepenverklaring"}

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        self.checkbox0 = QCheckBox("AP")
        self.checkbox0.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox0, 0, 0)

        self.checkbox1 = QCheckBox("BL")
        self.checkbox1.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox1, 1, 0)

        self.checkbox2 = QCheckBox("DD")
        self.checkbox2.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox2, 2, 0)

        self.checkbox3 = QCheckBox("ID")
        self.checkbox3.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox3, 3, 0)

        self.checkbox4 = QCheckBox("KD")
        self.checkbox4.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox4, 4, 0)

        self.checkbox5 = QCheckBox("KZ")
        self.checkbox5.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox5, 5, 0)

        self.checkbox6 = QCheckBox("ME")
        self.checkbox6.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox6, 6, 0)

        self.checkbox7 = QCheckBox("MP")
        self.checkbox7.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox7, 7, 0)

        self.checkbox8 = QCheckBox("PH")
        self.checkbox8.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox8, 8, 0)

        self.checkbox9 = QCheckBox("RS")
        self.checkbox9.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox9, 9, 0)

        self.checkbox10 = QCheckBox("WD")
        self.checkbox10.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox10, 10, 0)

        self.checkbox11 = QCheckBox("WH")
        self.checkbox11.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox11, 11, 0)

        self.checkbox12 = QCheckBox("WN")
        self.checkbox12.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox12, 12, 0)

        self.checkbox13 = QCheckBox("WZ")
        self.checkbox13.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox13, 13, 0)


        self.checkbox14 = QCheckBox("B1")
        self.checkbox14.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox14, 14, 0)

        self.checkbox15 = QCheckBox("B2")
        self.checkbox15.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox15, 15, 0)

        self.checkbox16 = QCheckBox("B3")
        self.checkbox16.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox16, 16, 0)

        self.checkbox17 = QCheckBox("B4")
        self.checkbox17.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox17, 17, 0)

        self.checkbox18 = QCheckBox("B5")
        self.checkbox18.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox18, 18, 0)


        self.checkbox19 = QCheckBox("E")
        self.checkbox19.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox19, 19, 0)

        self.checkbox20 = QCheckBox("W")
        self.checkbox20.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox20, 20, 0)


        self.checkbox21 = QCheckBox("1")
        self.checkbox21.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox21, 21, 0)

        self.checkbox22 = QCheckBox("2")
        self.checkbox22.toggled.connect(self.checkbox_toggled)
        layout.addWidget(self.checkbox22, 22, 0)

        self.QPushButton1 = QPushButton("click")
        self.QPushButton1.clicked.connect(self.btnPushed)
        layout.addWidget(self.QPushButton1, 23, 0)

    def checkbox_toggled(self):
        checked = {0: self.checkbox0,1: self.checkbox1,2: self.checkbox2,3: self.checkbox3,4: self.checkbox4,5: self.checkbox5,6: self.checkbox6,7: self.checkbox7,8: self.checkbox8,9: self.checkbox9,10: self.checkbox10,11: self.checkbox11,12: self.checkbox12,13: self.checkbox13, 14: self.checkbox14, 15: self.checkbox15, 16: self.checkbox16, 17: self.checkbox17, 18: self.checkbox18, 19: self.checkbox19,20: self.checkbox20, 21: self.checkbox21, 22: self.checkbox22}

        for i in range(len(checked)):
            checkbox = checked[i]
            if checkbox.isChecked():
                if checkbox.text() in L_Code and checkbox.text() not in Locate:
                    Locate.append(checkbox.text())
                elif checkbox.text() in B_Code and checkbox.text() not in B_disc:
                    B_disc.append(checkbox.text())
                elif checkbox.text() in X_Code and checkbox.text() not in X_disc:
                    X_disc.append(checkbox.text())
                elif checkbox.text() in X_Kind and checkbox.text() not in X_kind:
                    X_kind.append(checkbox.text())    
            else:
                if not checkbox.isChecked() and checkbox.text() in Locate:
                    Locate.remove(checkbox.text())
                elif not checkbox.isChecked() and checkbox.text() in B_disc:
                    B_disc.remove(checkbox.text())
                elif not checkbox.isChecked() and checkbox.text() in X_disc:
                    X_disc.remove(checkbox.text())
                elif not checkbox.isChecked() and checkbox.text() in X_kind:
                    X_kind.remove(checkbox.text())

    def btnPushed(self):
        Locate.sort()
        print(Locate)
        B_disc.sort()
        print(B_disc)
        X_disc.sort()
        print(X_disc)
        X_kind.sort()
        print(X_kind)
        for L in Locate:
            print(L_Code[L])
            time.sleep(0.1)
            for B in B_disc:
                print('\t', B_Code[B])
            for X in X_disc:
                print('\t', X_Code[X])
                time.sleep(0.1)
                for K in X_kind:
                    print('\t\t', X_Kind[K])
                    time.sleep(0.1)

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())