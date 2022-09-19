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
        # self.ui.label.setStyleSheet("background-image: url(fon.png);")
        # self.ui.pushButton.setStyleSheet(design.knopka)
        self.paused, self.mp3_url = True, ''
        self.SongList = []
        self.player   = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))           
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.PlayMode)
        self.timer.start(1000)
         
        self.start()                            
                                     
    def start(self):
        self.ui = uic.loadUi("inter5.ui")
        self.ui.pushButton.clicked.connect(self.MusicPlay)
        self.ui.pushButton_2.clicked.connect(self.open_folder)
        self.ui.pushButton_7.clicked.connect(self.MusicNext)
        self.ui.pushButton_6.clicked.connect(self.MusicPreview)
        self.ui.pushButton_5.clicked.connect(self.MusicStop)
        self.ui.pushButton_4.clicked.connect(self.music_pause)
        self.ui.listWidget.itemDoubleClicked.connect(self.play_duble)
        self.ui.show()
        
        
    def PlayMode(self):
        if self.player.position() == self.player.duration() and self.player.duration()!=0:
            self.MusicNext()    
               
    def open_folder(self):
        self.directory = QFileDialog.getExistingDirectory()
        if self.directory:
            for dirpath, dirnames, filenames in os.walk(self.directory):
                for file in filenames:
                    if file.endswith('mp3'):
                        self.SongList.append(os.path.join(dirpath, file).replace('\\','/'))
                        self.ui.listWidget.addItem(os.path.join(dirpath, file).replace('\\','/'))
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget.setCurrentItem(self.ui.listWidget.item(0))
        self.paused = True    
                        
    def play_duble(self):
        self.Preview_Next = True
        self.mp3_url = self.SongList[self.ui.listWidget.currentRow()]
        self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
        self.MusicPlay()
        self.Preview_Next = False
        
    def MusicPlay(self):
        self.paused = True
        self.mp3_url = self.SongList[self.ui.listWidget.currentRow()]
        self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
        self.player.play()
        
    def music_pause(self):
        if self.paused:
            self.player.pause()
            self.paused = False
        else:
            self.player.play()
            self.paused = True
        
    def MusicNext(self):
        if self.ui.listWidget.currentRow() != self.ui.listWidget.count()-1:
            self.ui.listWidget.setCurrentRow(self.ui.listWidget.currentRow()+1)
            # self.Preview_Next = True
            self.mp3_url      = self.SongList[self.ui.listWidget.currentRow()]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False
        else:
            self.ui.listWidget.setCurrentRow(0)
            self.Preview_Next = True
            self.mp3_url      = self.SongList[self.ui.listWidget.currentRow()]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False
            
    def MusicPreview(self):
        if self.ui.listWidget.currentRow()!=0:
            self.ui.listWidget.setCurrentRow(self.ui.listWidget.currentRow()-1)
            self.Preview_Next = True
            self.mp3_url = self.SongList[self.ui.listWidget.currentRow()]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False
        else:
            self.ui.listWidget.setCurrentRow(self.ui.listWidget.count() - 1)
            self.Preview_Next = True
            self.mp3_url = self.SongList[self.ui.listWidget.currentRow()]
            self.player.setMedia(QMediaContent(QUrl(self.mp3_url)))
            self.MusicPlay()
            self.Preview_Next = False
            
    def MusicStop(self):
        self.player.stop()
        self.ui.listWidget.setCurrentRow(0)
        self.ui.listWidget.setCurrentItem(self.ui.listWidget.item(0))
        
            
if __name__=='__main__':
	app = QApplication(sys.argv)
	ex=App()
	app.exec_()

