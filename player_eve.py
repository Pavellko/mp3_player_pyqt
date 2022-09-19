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
        self.ui = uic.loadUi("inter3.ui")
        self.ui.pushButton_2.clicked.connect(self.open_folder)
        self.ui.show()
        
    def open_folder(self):
        directory = QFileDialog.getExistingDirectory()
        if directory:
            for dirpath, dirnames, filenames in os.walk(directory):
                for file in filenames:
                    if file.endswith('mp3'):
                        self.ui.listWidget.addItem(os.path.join(dirpath, file))    


if __name__=='__main__':
	app = QApplication(sys.argv)
	ex=App()
	app.exec_()

