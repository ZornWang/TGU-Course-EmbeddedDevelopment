# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from Ui_ttt import Ui_Dialog

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random 
from my_label import *



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
       
    #初始化一个定时器
        self.timer=QTimer()
        #定时器结束，触发showTime方法
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.lab_clicked_n=0
        self.llabel = MyQLabel(self)
        self.llabel.setGeometry(200,200,250,250)
        self.llabel.setText("test")
        self.llabel.connect_customized_slot(self.slot_label_clicked)
    
    @pyqtSlot()
    def   slot_label_clicked(self):
        print("label clicked")  
        self.lab_clicked_n=self.lab_clicked_n+1
        self.llabel.setText("test"+str(self.lab_clicked_n)) 
    @pyqtSlot()
    def slot1(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        pix = QPixmap('111.png')  
        painter=QPainter()
        painter.begin(pix)
          
        pen = QPen(Qt.red, 5, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20, 20, 250, 200)     
        painter.end()
        self.label.setPixmap(pix)
        
        print("do it 1")
    
    @pyqtSlot()
    def slot2(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        x=random.randint(0,9)*20
        y=random.randint(0,9)*20
        print(x)
        print(y)
        self.pushButton_2.move(x, y)    
        #self.pushButton_2.setGeometry(x*20,y*20,50,50)
    @pyqtSlot()
    def slot3(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        #raise NotImplementedError
        print("do it 3ff")
        self.timer.start(1000)
    @pyqtSlot()    
    def showTime(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        time=QDateTime.currentDateTime()
        timeDisplay=time.toString('yyyy-MM-dd hh:mm:ss dddd')
        #在标签上显示时间
        self.textEdit.setText(timeDisplay)
        x=random.randint(0,9)
        y=random.randint(0,9)
       # print(x)
        #print(y)
            
       # self.pushButton_2.setGeometry(x*20,y*20,50,50)
        
if __name__ == "__main__": 
    import sys
    from PyQt5.QtWidgets import  QApplication
    app = QApplication(sys.argv)
    window = Dialog()  ### mydlg是main.py的上部的Class的名字
    window.show()
    sys.exit(app.exec_())
