# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog
from Ui_form import Ui_Dialog
import board
import busio
import adafruit_adxl34x
import numpy as np

class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)

        self.timer = QTimer()
        # 定时器结束，触发showTime方法
        self.timer.timeout.connect(self.Timmer)
        self.timer.start(100)

        self.g = 9.8

    def Timmer(self):
        self.Acceleration()

    def Acceleration(self):
        i2c = busio.I2C(board.SCL, board.SDA)
        acc = adafruit_adxl34x.ADXL345(i2c)
        x, y, z = acc.acceleration
        ax, ay, az = self.calAcceleration(x), self.calAcceleration(y), self.calAcceleration(z)
        self.showAcceleration(ax, ay, az)
        nx, ny, nz = self.calAngel(x), self.calAngel(y), self.calAngel(z)
        self.showAngel(nx,ny,nz)

    def calAcceleration(self, num):
        return str(num / self.g)[0:4]+'g'

    def calAngel(self,num):
        x = str(np.degrees(np.arccos(num/self.g)))
        # x = x[0:x.find('.')+2]
        if x == str(np.nan):
            x = '0'
            return x+'°'
        return x[0:x.find('.')+2]+'°'

    def showAcceleration(self, x, y, z):
        self.labelx.setText(x)
        self.labely.setText(y)
        self.labelz.setText(z)

    def showAngel(self, x, y, z):
        self.labelax.setText(x)
        self.labelay.setText(y)
        self.labelaz.setText(z)

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Dialog()  ### mydlg是main.py的上部的Class的名字
    window.show()
    sys.exit(app.exec_())
