from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 484)
        Dialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../Afbeeldingen/Icons/iconfinder_document_text_accept_103510.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.Checklist_Name = QtWidgets.QLineEdit(Dialog)
        self.Checklist_Name.setGeometry(QtCore.QRect(10, 20, 126, 23))
        self.Checklist_Name.setObjectName("Checklist_Name")
        self.Type_1 = QtWidgets.QLineEdit(Dialog)
        self.Type_1.setGeometry(QtCore.QRect(60, 60, 133, 20))
        self.Type_1.setObjectName("Type_1")
        self.Type_2 = QtWidgets.QLineEdit(Dialog)
        self.Type_2.setGeometry(QtCore.QRect(225, 60, 133, 20))
        self.Type_2.setObjectName("Type_2")
        self.Type_3 = QtWidgets.QLineEdit(Dialog)
        self.Type_3.setGeometry(QtCore.QRect(391, 60, 133, 20))
        self.Type_3.setObjectName("Type_3")
        self.AP = QtWidgets.QCheckBox(Dialog)
        self.AP.setGeometry(QtCore.QRect(20, 101, 36, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.AP.setFont(font)
        self.AP.setChecked(True)
        self.AP.setObjectName("AP")
        self.CBT1_1 = QtWidgets.QCheckBox(Dialog)
        self.CBT1_1.setGeometry(QtCore.QRect(70, 100, 60, 17))
        font = QtGui.QFont()
        self.CBT1_1.setFont(font)
        self.CBT1_1.setObjectName("CBT1_1")
        self.checkBox_3 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_3.setGeometry(QtCore.QRect(400, 101, 60, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_4.setGeometry(QtCore.QRect(230, 123, 60, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.BL = QtWidgets.QCheckBox(Dialog)
        self.BL.setGeometry(QtCore.QRect(20, 124, 34, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BL.setFont(font)
        self.BL.setChecked(True)
        self.BL.setObjectName("BL")
        self.checkBox_6 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_6.setGeometry(QtCore.QRect(400, 124, 60, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_7.setGeometry(QtCore.QRect(230, 146, 60, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_8.setGeometry(QtCore.QRect(20, 147, 37, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_8.setFont(font)
        self.checkBox_8.setChecked(True)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_9.setGeometry(QtCore.QRect(400, 147, 60, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.CBT2_4 = QtWidgets.QCheckBox(Dialog)
        self.CBT2_4.setGeometry(QtCore.QRect(230, 169, 60, 17))
        self.CBT2_4.setObjectName("CBT2_4")
        self.ID = QtWidgets.QCheckBox(Dialog)
        self.ID.setGeometry(QtCore.QRect(20, 170, 34, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ID.setFont(font)
        self.ID.setChecked(True)
        self.ID.setObjectName("ID")
        self.CBT3_4 = QtWidgets.QCheckBox(Dialog)
        self.CBT3_4.setGeometry(QtCore.QRect(400, 170, 60, 17))
        self.CBT3_4.setObjectName("CBT3_4")
        self.checkBox_13 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_13.setGeometry(QtCore.QRect(230, 192, 60, 17))
        self.checkBox_13.setObjectName("checkBox_13")
        self.WZ = QtWidgets.QCheckBox(Dialog)
        self.WZ.setGeometry(QtCore.QRect(20, 193, 39, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WZ.setFont(font)
        self.WZ.setChecked(True)
        self.WZ.setObjectName("WZ")
        self.checkBox_15 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_15.setGeometry(QtCore.QRect(400, 193, 60, 17))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_16.setGeometry(QtCore.QRect(230, 215, 60, 17))
        self.checkBox_16.setObjectName("checkBox_16")
        self.KD = QtWidgets.QCheckBox(Dialog)
        self.KD.setGeometry(QtCore.QRect(20, 216, 36, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.KD.setFont(font)
        self.KD.setChecked(True)
        self.KD.setObjectName("KD")
        self.checkBox_18 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_18.setGeometry(QtCore.QRect(400, 216, 60, 17))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_19.setGeometry(QtCore.QRect(230, 238, 60, 17))
        self.checkBox_19.setObjectName("checkBox_19")
        self.KZ = QtWidgets.QCheckBox(Dialog)
        self.KZ.setGeometry(QtCore.QRect(20, 239, 35, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.KZ.setFont(font)
        self.KZ.setChecked(True)
        self.KZ.setObjectName("KZ")
        self.checkBox_21 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_21.setGeometry(QtCore.QRect(400, 239, 60, 17))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_22.setGeometry(QtCore.QRect(230, 261, 60, 17))
        self.checkBox_22.setObjectName("checkBox_22")
        self.ME = QtWidgets.QCheckBox(Dialog)
        self.ME.setGeometry(QtCore.QRect(20, 262, 37, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ME.setFont(font)
        self.ME.setChecked(True)
        self.ME.setObjectName("ME")
        self.checkBox_24 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_24.setGeometry(QtCore.QRect(400, 262, 60, 17))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_25.setGeometry(QtCore.QRect(230, 285, 60, 17))
        self.checkBox_25.setObjectName("checkBox_25")
        self.MP = QtWidgets.QCheckBox(Dialog)
        self.MP.setGeometry(QtCore.QRect(20, 286, 37, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.MP.setFont(font)
        self.MP.setChecked(True)
        self.MP.setObjectName("MP")
        self.checkBox_27 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_27.setGeometry(QtCore.QRect(400, 286, 60, 17))
        self.checkBox_27.setObjectName("checkBox_27")
        self.checkBox_28 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_28.setGeometry(QtCore.QRect(230, 308, 66, 17))
        self.checkBox_28.setObjectName("checkBox_28")
        self.PH = QtWidgets.QCheckBox(Dialog)
        self.PH.setGeometry(QtCore.QRect(20, 309, 36, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PH.setFont(font)
        self.PH.setChecked(True)
        self.PH.setObjectName("PH")
        self.checkBox_30 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_30.setGeometry(QtCore.QRect(400, 309, 66, 17))
        self.checkBox_30.setObjectName("checkBox_30")
        self.checkBox_31 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_31.setGeometry(QtCore.QRect(230, 331, 66, 17))
        self.checkBox_31.setObjectName("checkBox_31")
        self.PL = QtWidgets.QCheckBox(Dialog)
        self.PL.setGeometry(QtCore.QRect(20, 332, 34, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.PL.setFont(font)
        self.PL.setChecked(True)
        self.PL.setObjectName("PL")
        self.checkBox_33 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_33.setGeometry(QtCore.QRect(400, 332, 66, 17))
        self.checkBox_33.setObjectName("checkBox_33")
        self.checkBox_34 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_34.setGeometry(QtCore.QRect(230, 354, 66, 17))
        self.checkBox_34.setObjectName("checkBox_34")
        self.RS = QtWidgets.QCheckBox(Dialog)
        self.RS.setGeometry(QtCore.QRect(20, 355, 36, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.RS.setFont(font)
        self.RS.setChecked(True)
        self.RS.setObjectName("RS")
        self.checkBox_36 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_36.setGeometry(QtCore.QRect(400, 355, 66, 17))
        self.checkBox_36.setObjectName("checkBox_36")
        self.checkBox_37 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_37.setGeometry(QtCore.QRect(230, 377, 66, 17))
        self.checkBox_37.setObjectName("checkBox_37")
        self.WH = QtWidgets.QCheckBox(Dialog)
        self.WH.setGeometry(QtCore.QRect(20, 378, 40, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WH.setFont(font)
        self.WH.setChecked(True)
        self.WH.setObjectName("WH")
        self.checkBox_39 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_39.setGeometry(QtCore.QRect(400, 378, 66, 17))
        self.checkBox_39.setObjectName("checkBox_39")
        self.checkBox_40 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_40.setGeometry(QtCore.QRect(230, 400, 66, 17))
        self.checkBox_40.setObjectName("checkBox_40")
        self.WN = QtWidgets.QCheckBox(Dialog)
        self.WN.setGeometry(QtCore.QRect(20, 401, 40, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WN.setFont(font)
        self.WN.setChecked(True)
        self.WN.setObjectName("WN")
        self.checkBox_42 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_42.setGeometry(QtCore.QRect(400, 401, 66, 17))
        self.checkBox_42.setObjectName("checkBox_42")
        self.checkBox_43 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_43.setGeometry(QtCore.QRect(230, 423, 66, 17))
        self.checkBox_43.setObjectName("checkBox_43")
        self.WD = QtWidgets.QCheckBox(Dialog)
        self.WD.setGeometry(QtCore.QRect(20, 424, 40, 17))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WD.setFont(font)
        self.WD.setChecked(True)
        self.WD.setObjectName("WD")
        self.checkBox_45 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_45.setGeometry(QtCore.QRect(400, 424, 66, 17))
        self.checkBox_45.setObjectName("checkBox_45")
        self.checkBox_46 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_46.setGeometry(QtCore.QRect(70, 377, 66, 17))
        self.checkBox_46.setObjectName("checkBox_46")
        self.checkBox_47 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_47.setGeometry(QtCore.QRect(70, 238, 60, 17))
        self.checkBox_47.setObjectName("checkBox_47")
        self.checkBox_48 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_48.setGeometry(QtCore.QRect(70, 123, 60, 17))
        self.checkBox_48.setObjectName("checkBox_48")
        self.checkBox_49 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_49.setGeometry(QtCore.QRect(70, 285, 60, 17))
        self.checkBox_49.setObjectName("checkBox_49")
        self.checkBox_50 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_50.setGeometry(QtCore.QRect(70, 261, 60, 17))
        self.checkBox_50.setObjectName("checkBox_50")
        self.checkBox_51 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_51.setGeometry(QtCore.QRect(70, 146, 60, 17))
        self.checkBox_51.setObjectName("checkBox_51")
        self.checkBox_52 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_52.setGeometry(QtCore.QRect(70, 354, 66, 17))
        self.checkBox_52.setObjectName("checkBox_52")
        self.checkBox_53 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_53.setGeometry(QtCore.QRect(70, 215, 60, 17))
        self.checkBox_53.setObjectName("checkBox_53")
        self.checkBox_54 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_54.setGeometry(QtCore.QRect(70, 423, 66, 17))
        self.checkBox_54.setObjectName("checkBox_54")
        self.checkBox_55 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_55.setGeometry(QtCore.QRect(230, 100, 60, 17))
        self.checkBox_55.setObjectName("checkBox_55")
        self.checkBox_56 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_56.setGeometry(QtCore.QRect(70, 400, 66, 17))
        self.checkBox_56.setObjectName("checkBox_56")
        self.checkBox_57 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_57.setGeometry(QtCore.QRect(70, 192, 60, 17))
        self.checkBox_57.setObjectName("checkBox_57")
        self.checkBox_58 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_58.setGeometry(QtCore.QRect(70, 308, 66, 17))
        self.checkBox_58.setObjectName("checkBox_58")
        self.checkBox_59 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_59.setGeometry(QtCore.QRect(70, 169, 60, 17))
        self.checkBox_59.setObjectName("checkBox_59")
        self.checkBox_60 = QtWidgets.QCheckBox(Dialog)
        self.checkBox_60.setGeometry(QtCore.QRect(70, 331, 66, 17))
        self.checkBox_60.setObjectName("checkBox_60")
        self.Save = QtWidgets.QPushButton(Dialog)
        self.Save.setGeometry(QtCore.QRect(370, 20, 75, 23))
        self.Save.setObjectName("Save")
        self.Open = QtWidgets.QPushButton(Dialog)
        self.Open.setGeometry(QtCore.QRect(450, 20, 75, 23))
        self.Open.setObjectName("Open")
        self.dateEdit = QtWidgets.QDateEdit(Dialog)
        self.dateEdit.setGeometry(QtCore.QRect(150, 20, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(270, 20, 91, 22))
        self.comboBox.setEditable(True)
        self.comboBox.setMaxCount(999999)
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.Checklist_Name, self.dateEdit)
        Dialog.setTabOrder(self.dateEdit, self.comboBox)
        Dialog.setTabOrder(self.comboBox, self.Save)
        Dialog.setTabOrder(self.Save, self.Open)
        Dialog.setTabOrder(self.Open, self.Type_1)
        Dialog.setTabOrder(self.Type_1, self.Type_2)
        Dialog.setTabOrder(self.Type_2, self.Type_3)
        Dialog.setTabOrder(self.Type_3, self.AP)
        Dialog.setTabOrder(self.AP, self.BL)
        Dialog.setTabOrder(self.BL, self.checkBox_8)
        Dialog.setTabOrder(self.checkBox_8, self.ID)
        Dialog.setTabOrder(self.ID, self.WZ)
        Dialog.setTabOrder(self.WZ, self.KD)
        Dialog.setTabOrder(self.KD, self.KZ)
        Dialog.setTabOrder(self.KZ, self.ME)
        Dialog.setTabOrder(self.ME, self.MP)
        Dialog.setTabOrder(self.MP, self.PH)
        Dialog.setTabOrder(self.PH, self.PL)
        Dialog.setTabOrder(self.PL, self.RS)
        Dialog.setTabOrder(self.RS, self.WH)
        Dialog.setTabOrder(self.WH, self.WN)
        Dialog.setTabOrder(self.WN, self.WD)
        Dialog.setTabOrder(self.WD, self.CBT1_1)
        Dialog.setTabOrder(self.CBT1_1, self.checkBox_55)
        Dialog.setTabOrder(self.checkBox_55, self.checkBox_3)
        Dialog.setTabOrder(self.checkBox_3, self.checkBox_48)
        Dialog.setTabOrder(self.checkBox_48, self.checkBox_4)
        Dialog.setTabOrder(self.checkBox_4, self.checkBox_6)
        Dialog.setTabOrder(self.checkBox_6, self.checkBox_51)
        Dialog.setTabOrder(self.checkBox_51, self.checkBox_7)
        Dialog.setTabOrder(self.checkBox_7, self.checkBox_9)
        Dialog.setTabOrder(self.checkBox_9, self.checkBox_59)
        Dialog.setTabOrder(self.checkBox_59, self.CBT2_4)
        Dialog.setTabOrder(self.CBT2_4, self.CBT3_4)
        Dialog.setTabOrder(self.CBT3_4, self.checkBox_57)
        Dialog.setTabOrder(self.checkBox_57, self.checkBox_13)
        Dialog.setTabOrder(self.checkBox_13, self.checkBox_15)
        Dialog.setTabOrder(self.checkBox_15, self.checkBox_53)
        Dialog.setTabOrder(self.checkBox_53, self.checkBox_16)
        Dialog.setTabOrder(self.checkBox_16, self.checkBox_18)
        Dialog.setTabOrder(self.checkBox_18, self.checkBox_47)
        Dialog.setTabOrder(self.checkBox_47, self.checkBox_19)
        Dialog.setTabOrder(self.checkBox_19, self.checkBox_21)
        Dialog.setTabOrder(self.checkBox_21, self.checkBox_50)
        Dialog.setTabOrder(self.checkBox_50, self.checkBox_22)
        Dialog.setTabOrder(self.checkBox_22, self.checkBox_24)
        Dialog.setTabOrder(self.checkBox_24, self.checkBox_49)
        Dialog.setTabOrder(self.checkBox_49, self.checkBox_25)
        Dialog.setTabOrder(self.checkBox_25, self.checkBox_27)
        Dialog.setTabOrder(self.checkBox_27, self.checkBox_58)
        Dialog.setTabOrder(self.checkBox_58, self.checkBox_28)
        Dialog.setTabOrder(self.checkBox_28, self.checkBox_30)
        Dialog.setTabOrder(self.checkBox_30, self.checkBox_60)
        Dialog.setTabOrder(self.checkBox_60, self.checkBox_31)
        Dialog.setTabOrder(self.checkBox_31, self.checkBox_33)
        Dialog.setTabOrder(self.checkBox_33, self.checkBox_52)
        Dialog.setTabOrder(self.checkBox_52, self.checkBox_34)
        Dialog.setTabOrder(self.checkBox_34, self.checkBox_36)
        Dialog.setTabOrder(self.checkBox_36, self.checkBox_46)
        Dialog.setTabOrder(self.checkBox_46, self.checkBox_37)
        Dialog.setTabOrder(self.checkBox_37, self.checkBox_39)
        Dialog.setTabOrder(self.checkBox_39, self.checkBox_56)
        Dialog.setTabOrder(self.checkBox_56, self.checkBox_40)
        Dialog.setTabOrder(self.checkBox_40, self.checkBox_42)
        Dialog.setTabOrder(self.checkBox_42, self.checkBox_54)
        Dialog.setTabOrder(self.checkBox_54, self.checkBox_43)
        Dialog.setTabOrder(self.checkBox_43, self.checkBox_45)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CheckIt"))
        self.AP.setText(_translate("Dialog", "AP"))
        self.CBT1_1.setText(_translate("Dialog", "CBT1_1"))
        self.checkBox_3.setText(_translate("Dialog", "CBT3_1"))
        self.checkBox_4.setText(_translate("Dialog", "CBT2_2"))
        self.BL.setText(_translate("Dialog", "BL"))
        self.checkBox_6.setText(_translate("Dialog", "CBT3_2"))
        self.checkBox_7.setText(_translate("Dialog", "CBT2_3"))
        self.checkBox_8.setText(_translate("Dialog", "DD"))
        self.checkBox_9.setText(_translate("Dialog", "CBT3_3"))
        self.CBT2_4.setText(_translate("Dialog", "CBT2_4"))
        self.ID.setText(_translate("Dialog", "ID"))
        self.CBT3_4.setText(_translate("Dialog", "CBT3_4"))
        self.checkBox_13.setText(_translate("Dialog", "CBT2_5"))
        self.WZ.setText(_translate("Dialog", "WZ"))
        self.checkBox_15.setText(_translate("Dialog", "CBT3_5"))
        self.checkBox_16.setText(_translate("Dialog", "CBT2_6"))
        self.KD.setText(_translate("Dialog", "KD"))
        self.checkBox_18.setText(_translate("Dialog", "CBT3_6"))
        self.checkBox_19.setText(_translate("Dialog", "CBT2_7"))
        self.KZ.setText(_translate("Dialog", "KZ"))
        self.checkBox_21.setText(_translate("Dialog", "CBT3_7"))
        self.checkBox_22.setText(_translate("Dialog", "CBT2_8"))
        self.ME.setText(_translate("Dialog", "ME"))
        self.checkBox_24.setText(_translate("Dialog", "CBT3_8"))
        self.checkBox_25.setText(_translate("Dialog", "CBT2_9"))
        self.MP.setText(_translate("Dialog", "MP"))
        self.checkBox_27.setText(_translate("Dialog", "CBT3_9"))
        self.checkBox_28.setText(_translate("Dialog", "CBT2_10"))
        self.PH.setText(_translate("Dialog", "PH"))
        self.checkBox_30.setText(_translate("Dialog", "CBT3_10"))
        self.checkBox_31.setText(_translate("Dialog", "CBT2_11"))
        self.PL.setText(_translate("Dialog", "PL"))
        self.checkBox_33.setText(_translate("Dialog", "CBT3_11"))
        self.checkBox_34.setText(_translate("Dialog", "CBT2_12"))
        self.RS.setText(_translate("Dialog", "RS"))
        self.checkBox_36.setText(_translate("Dialog", "CBT3_12"))
        self.checkBox_37.setText(_translate("Dialog", "CBT2_13"))
        self.WH.setText(_translate("Dialog", "WH"))
        self.checkBox_39.setText(_translate("Dialog", "CBT3_13"))
        self.checkBox_40.setText(_translate("Dialog", "CBT2_14"))
        self.WN.setText(_translate("Dialog", "WN"))
        self.checkBox_42.setText(_translate("Dialog", "CBT3_14"))
        self.checkBox_43.setText(_translate("Dialog", "CBT2_15"))
        self.WD.setText(_translate("Dialog", "WD"))
        self.checkBox_45.setText(_translate("Dialog", "CBT3_15"))
        self.checkBox_46.setText(_translate("Dialog", "CBT1_13"))
        self.checkBox_47.setText(_translate("Dialog", "CBT1_7"))
        self.checkBox_48.setText(_translate("Dialog", "CBT1_2"))
        self.checkBox_49.setText(_translate("Dialog", "CBT1_9"))
        self.checkBox_50.setText(_translate("Dialog", "CBT1_8"))
        self.checkBox_51.setText(_translate("Dialog", "CBT1_3"))
        self.checkBox_52.setText(_translate("Dialog", "CBT1_12"))
        self.checkBox_53.setText(_translate("Dialog", "CBT1_6"))
        self.checkBox_54.setText(_translate("Dialog", "CBT1_15"))
        self.checkBox_55.setText(_translate("Dialog", "CBT2_1"))
        self.checkBox_56.setText(_translate("Dialog", "CBT1_14"))
        self.checkBox_57.setText(_translate("Dialog", "CBT1_5"))
        self.checkBox_58.setText(_translate("Dialog", "CBT1_10"))
        self.checkBox_59.setText(_translate("Dialog", "CBT1_4"))
        self.checkBox_60.setText(_translate("Dialog", "CBT1_11"))
        self.Save.setText(_translate("Dialog", "Save"))
        self.Open.setText(_translate("Dialog", "Open"))
        self.comboBox.setCurrentText(_translate("Dialog", "Selecteer"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    app.exec_()
