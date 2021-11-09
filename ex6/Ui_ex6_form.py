# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/lab/ex6/ex6_form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(205, 215)
        Dialog.setSizeGripEnabled(True)
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(0, 10, 201, 41))
        self.textEdit.setObjectName("textEdit")
        self.Blinkbtn = QtWidgets.QPushButton(Dialog)
        self.Blinkbtn.setGeometry(QtCore.QRect(0, 60, 201, 30))
        self.Blinkbtn.setObjectName("Blinkbtn")
        self.LightOnbtn = QtWidgets.QPushButton(Dialog)
        self.LightOnbtn.setGeometry(QtCore.QRect(0, 100, 201, 30))
        self.LightOnbtn.setObjectName("LightOnbtn")
        self.LightOffbtn = QtWidgets.QPushButton(Dialog)
        self.LightOffbtn.setGeometry(QtCore.QRect(0, 140, 201, 30))
        self.LightOffbtn.setObjectName("LightOffbtn")
        self.HelloWorldbtn = QtWidgets.QPushButton(Dialog)
        self.HelloWorldbtn.setGeometry(QtCore.QRect(0, 180, 99, 30))
        self.HelloWorldbtn.setObjectName("HelloWorldbtn")
        self.Closebtn = QtWidgets.QPushButton(Dialog)
        self.Closebtn.setGeometry(QtCore.QRect(100, 180, 99, 30))
        self.Closebtn.setObjectName("Closebtn")

        self.retranslateUi(Dialog)
        self.Blinkbtn.clicked.connect(Dialog.Blink)
        self.Closebtn.clicked.connect(Dialog.close)
        self.HelloWorldbtn.clicked.connect(Dialog.printHelloWorld)
        self.LightOffbtn.clicked.connect(Dialog.LightOff)
        self.LightOnbtn.clicked.connect(Dialog.LightOn)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Blinkbtn.setText(_translate("Dialog", "Blink"))
        self.LightOnbtn.setText(_translate("Dialog", "LightOn"))
        self.LightOffbtn.setText(_translate("Dialog", "LightOff"))
        self.HelloWorldbtn.setText(_translate("Dialog", "HelloWorld"))
        self.Closebtn.setText(_translate("Dialog", "Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

