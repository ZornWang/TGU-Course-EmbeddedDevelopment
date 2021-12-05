# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/lab/ex8/form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(340, 494)
        Dialog.setSizeGripEnabled(True)
        self.cam = QtWidgets.QLabel(Dialog)
        self.cam.setGeometry(QtCore.QRect(10, 10, 320, 240))
        self.cam.setText("")
        self.cam.setAlignment(QtCore.Qt.AlignCenter)
        self.cam.setObjectName("cam")
        self.shot = QtWidgets.QPushButton(Dialog)
        self.shot.setGeometry(QtCore.QRect(10, 280, 320, 30))
        self.shot.setObjectName("shot")
        self.turnToGary = QtWidgets.QPushButton(Dialog)
        self.turnToGary.setGeometry(QtCore.QRect(10, 330, 150, 30))
        self.turnToGary.setObjectName("turnToGary")
        self.color = QtWidgets.QLabel(Dialog)
        self.color.setGeometry(QtCore.QRect(180, 380, 150, 30))
        self.color.setText("")
        self.color.setAlignment(QtCore.Qt.AlignCenter)
        self.color.setObjectName("color")
        self.back = QtWidgets.QPushButton(Dialog)
        self.back.setGeometry(QtCore.QRect(180, 330, 150, 30))
        self.back.setObjectName("back")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 380, 151, 30))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.code = QtWidgets.QTextBrowser(Dialog)
        self.code.setGeometry(QtCore.QRect(10, 430, 321, 51))
        self.code.setObjectName("code")

        self.retranslateUi(Dialog)
        self.shot.clicked.connect(Dialog.shotPic)
        self.turnToGary.clicked.connect(Dialog.turnGary)
        self.back.clicked.connect(Dialog.backToCam)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.shot.setText(_translate("Dialog", "Shot"))
        self.turnToGary.setText(_translate("Dialog", "Turn to gary"))
        self.back.setText(_translate("Dialog", "Back"))
        self.label.setText(_translate("Dialog", "Center Color : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

