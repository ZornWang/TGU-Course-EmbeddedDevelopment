# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""
import time

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_ex6_form import Ui_Dialog

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
pin = 21
GPIO.setup(pin,GPIO.OUT)

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
    
    @pyqtSlot()
    def Blink(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        for i in range(int(self.textEdit.toPlainText())):
            GPIO.output(pin,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pin, GPIO.LOW)
            time.sleep(0.5)
        # raise NotImplementedError
    
    @pyqtSlot()
    def LightOn(self):
        """
        Slot documentation goes here.
        """
        GPIO.output(pin,GPIO.HIGH)
        # TODO: not implemented yet
        # raise NotImplementedError
    
    @pyqtSlot()
    def LightOff(self):
        """
        Slot documentation goes here.
        """
        GPIO.output(pin,GPIO.LOW)
        # TODO: not implemented yet
        # raise NotImplementedError
    
    @pyqtSlot()
    def printHelloWorld(self):
        """
        Slot documentation goes here.
        """
        print("HelloWorld!")
        # TODO: not implemented yet
        # raise NotImplementedError

if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import  QApplication
    app = QApplication(sys.argv)
    window = Dialog()  ### mydlg是main.py的上部的Class的名字
    window.show()
    sys.exit(app.exec_())
