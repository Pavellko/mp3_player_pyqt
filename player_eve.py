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
        self.SongList = []
        self.player   = QMediaPlayer()
        self.mp3_url = ''
        self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))    
        self.start()                            
                                     
    def start(self):
        self.ui = uic.loadUi("inter5.ui")
        self.ui.pushButton_2.clicked.connect(self.open_folder)
        self.ui.listWidget.itemDoubleClicked.connect(self.play_song)
        self.ui.show()
        
    def open_folder(self):
        self.directory = QFileDialog.getExistingDirectory()
        if self.directory:
            for dirpath, dirnames, filenames in os.walk(self.directory):
                for file in filenames:
                    if file.endswith('mp3'):
                        self.SongList.append(os.path.join(dirpath, file).replace('\\','/'))
                        self.ui.listWidget.addItem(os.path.join(dirpath, file).replace('\\','/'))    
                        
    def play_song(self):
        self.mp3_url = self.SongList[self.ui.listWidget.currentRow()]
        self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
        self.MusicPlay()
        
    def MusicPlay(self):
        self.mp3_url = self.SongList[self.ui.listWidget.currentRow()]
        self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
        self.player.play()
            
if __name__=='__main__':
	app = QApplication(sys.argv)
	ex=App()
	app.exec_()

