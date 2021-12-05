# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/lab/ex7/adxl345/form.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(342, 279)
        Dialog.setSizeGripEnabled(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 160, 68, 22))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 200, 68, 22))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 240, 68, 22))
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.labelx = QtWidgets.QLabel(Dialog)
        self.labelx.setGeometry(QtCore.QRect(130, 160, 68, 22))
        self.labelx.setAlignment(QtCore.Qt.AlignCenter)
        self.labelx.setObjectName("labelx")
        self.labely = QtWidgets.QLabel(Dialog)
        self.labely.setGeometry(QtCore.QRect(130, 200, 68, 22))
        self.labely.setAlignment(QtCore.Qt.AlignCenter)
        self.labely.setObjectName("labely")
        self.labelz = QtWidgets.QLabel(Dialog)
        self.labelz.setGeometry(QtCore.QRect(130, 240, 68, 22))
        self.labelz.setAlignment(QtCore.Qt.AlignCenter)
        self.labelz.setObjectName("labelz")
        self.labelax = QtWidgets.QLabel(Dialog)
        self.labelax.setGeometry(QtCore.QRect(250, 160, 68, 22))
        self.labelax.setAlignment(QtCore.Qt.AlignCenter)
        self.labelax.setObjectName("labelax")
        self.labelay = QtWidgets.QLabel(Dialog)
        self.labelay.setGeometry(QtCore.QRect(250, 200, 68, 22))
        self.labelay.setAlignment(QtCore.Qt.AlignCenter)
        self.labelay.setObjectName("labelay")
        self.labelaz = QtWidgets.QLabel(Dialog)
        self.labelaz.setGeometry(QtCore.QRect(250, 240, 68, 22))
        self.labelaz.setAlignment(QtCore.Qt.AlignCenter)
        self.labelaz.setObjectName("labelaz")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(120, 120, 91, 22))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(250, 120, 68, 22))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(20, 120, 68, 22))
        self.label_9.setObjectName("label_9")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "X"))
        self.label_2.setText(_translate("Dialog", "Y"))
        self.label_3.setText(_translate("Dialog", "Z"))
        self.labelx.setText(_translate("Dialog", "TextLabel"))
        self.labely.setText(_translate("Dialog", "TextLabel"))
        self.labelz.setText(_translate("Dialog", "TextLabel"))
        self.labelax.setText(_translate("Dialog", "TextLabel"))
        self.labelay.setText(_translate("Dialog", "TextLabel"))
        self.labelaz.setText(_translate("Dialog", "TextLabel"))
        self.label_7.setText(_translate("Dialog", "Acceleration"))
        self.label_8.setText(_translate("Dialog", "Angle"))
        self.label_9.setText(_translate("Dialog", "Direction"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

