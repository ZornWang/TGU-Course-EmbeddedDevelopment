# -*- coding: utf-8 -*-

"""
Module implementing mydlg.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Ui_main_form import Ui_Dialog
import random 

class mydlg(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(mydlg, self).__init__(parent)
        self.setupUi(self)
        self.timer=QTimer()
        self.ctrl=0
        #定时器结束，触发showTime方法
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        
    
    @pyqtSlot()
    def showTime(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        if self.ctrl==0 :
            print("timer do 0 ")
        if self.ctrl==1 :
            print("timer do 1") 
      
        x=random.randint(0,9)
        y=random.randint(0,9)
        self.label.setGeometry(x*20,y*20,50,50) 
    
    
    @pyqtSlot()
    def on_pushButton_2_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("btn2 do ")
        self.ctrl=1
    
    @pyqtSlot()
    def on_btn1_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        print("btn1 do ")
        self.ctrl=0
        pix = QPixmap('111.png')
        self.label.setPixmap(pix)

        
if __name__ == "__main__": 
    import sys
    from PyQt5.QtWidgets import  QApplication
    app = QApplication(sys.argv)
    window = mydlg()  ### mydlg是main.py的上部的Class的名字
    window.show()
    sys.exit(app.exec_())
