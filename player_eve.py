import sys
import os
import configparser
import random
import time


from PyQt5.QtWidgets    import *
from PyQt5.QtGui        import *
from PyQt5.QtCore       import *
from PyQt5.QtMultimedia import *
from PyQt5 import uic
import design



class App(QWidget): 
    def __init__(self):
        super(App, self).__init__()
        self.start()
        # self.ui.label.setStyleSheet("background-image: url(fon.png);")
        # self.ui.pushButton.setStyleSheet(design.knopka)                                
                                     
    def start(self):
        self.ui = uic.loadUi("inter2.ui")
        self.ui.show()


if __name__=='__main__':
	app = QApplication(sys.argv)
	ex=App()
	app.exec_()



