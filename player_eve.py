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




class App(QWidget): 
    def __init__(self):
        super(App, self).__init__()
        self.start()
        self.ui.label.setStyleSheet("background-image: url(fon.png);")
        self.ui.pushButton.setStyleSheet("QPushButton#pushButton{\n"
                                         "background-image: url(knopka.png);\n"
                                         "font: 75 14pt 'Arial';\n"
                                         "color: rgb(255, 255, 206);\n"
                                         "border: none;\n"
                                         "}\n"
                                         "QPushButton#pushButton:pressed{\n"
	                                     "padding-left: 3px;\n"
	                                     "padding-top: 3px;\n"
                                         "}\n"                                         
                                         )
                                     
    def start(self):
        self.ui = uic.loadUi("inter2.ui")
        self.ui.show()


if __name__=='__main__':
	app = QApplication(sys.argv)
	ex=App()
	app.exec_()



