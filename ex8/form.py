# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog, QFileDialog
from PyQt5.QtGui import *
from Ui_form import Ui_Dialog
from PIL import Image, ImageQt
import numpy as np
import cv2

from pyzbar import pyzbar
import zxing


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

        self.camerTimer = QTimer()
        self.camerTimer.timeout.connect(self.initCam)
        self.camerTimer.start(10)

        self.colorTimer = QTimer()
        self.colorTimer.timeout.connect(self.getColor)
        self.colorTimer.start(1000)

        self.codeTimer = QTimer()
        self.codeTimer.timeout.connect(self.codeScanner)
        self.codeTimer.start(10)

        self.With = 320
        self.Hight = 240

        self.cap = cv2.VideoCapture(0)

        self.scanner = pyzbar._image_scanner()

        self.turnToGary.setEnabled(False)
        self.back.setEnabled(False)

    def openCam(self):
        ret, img, = self.cap.read()
        raw_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resize_img = cv2.resize(raw_img, (self.With, self.Hight), interpolation=cv2.INTER_AREA)
        cur_img = QImage(resize_img, self.With, self.Hight, self.With * 3, QImage.Format_RGB888)
        # print(type(raw_img))
        # print(type(resize_img))
        # print(type(cur_img))
        return img, cur_img

    def initCam(self):
        self.cam.setPixmap(QPixmap.fromImage(self.openCam()[1]))

    @pyqtSlot()
    def shotPic(self):
        self.camerTimer.stop()
        self.colorTimer.stop()
        self.codeTimer.stop()
        self.save_img = self.openCam()[0]
        self.cam.setPixmap(QPixmap.fromImage(self.openCam()[1]))
        self.turnToGary.setEnabled(True)
        self.back.setEnabled(True)

    @pyqtSlot()
    def turnGary(self):
        img = cv2.resize(self.save_img, (self.With, self.Hight), interpolation=cv2.INTER_AREA)
        img = np.array(img)
        img = img[:, :, 0]
        fromarray = Image.fromarray(img)
        gary_img = ImageQt.toqpixmap(fromarray)
        self.turnToGary.setEnabled(False)
        self.cam.setPixmap(gary_img)
        self.save_img = None

    @pyqtSlot()
    def backToCam(self):
        self.save_img = None
        self.camerTimer.start(10)
        self.colorTimer.start(1000)
        self.codeTimer.start(10)
        self.turnToGary.setEnabled(False)
        self.back.setEnabled(False)

    def getColor(self):
        center_pix = self.openCam()[1].pixel(self.With / 2, self.Hight / 2)
        center_pix_color = QColor(center_pix)
        self.color.setStyleSheet('background-color:' + center_pix_color.name() + ';')
        self.color.setText(center_pix_color.name())

    def codeScanner(self):
        pil = Image.fromarray(self.openCam()[0]).convert('L')
        decodes = pyzbar.decode(pil)
        for decode in decodes:
            decodeData = decode.data.decode('utf-8')
            self.code.setText(decodeData)


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = Dialog()  ### mydlg是main.py的上部的Class的名字
    window.show()
    sys.exit(app.exec_())
