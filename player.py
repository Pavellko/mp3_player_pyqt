from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pygame
import os, sys

app = QApplication([])
ui = uic.loadUi("inter.ui")

ui.setWindowTitle('Mp3 Player')
ui.setFixedSize(350, 500)
ui.show()

pygame.init()

flag = False
list_song = []

def open_file():
    file_name = QFileDialog()
    file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNames()
    song = names[0]
    ui.listWidget.addItems(song)

def play_song():
    global flag
    ui.pushButton_4.setStyleSheet("background-color: None")
    flag = True
    playlist = []
    ind = ui.listWidget.currentRow()
    zz = ui.listWidget.count()     
    for i in range(ind, zz):
        playlist.append(ui.listWidget.item(i).text())
    i = 0    
    pygame.mixer.music.load ( playlist[i] )    
    if len(playlist) != 1:
        i += 1        
        pygame.mixer.music.queue ( playlist[i] )   
        pygame.mixer.music.set_endevent ( pygame.USEREVENT ) 
        pygame.mixer.music.play()     
        running = True
        while running:
            for event in pygame.event.get():     
                if event.type == pygame.USEREVENT:   
                    if len ( playlist ) - i  > 1:
                        i +=1                        
                        pygame.mixer.music.queue ( playlist[i] )
    else:
        pygame.mixer.music.play()

def open_folder():
    directory = QFileDialog.getExistingDirectory()
    if directory:
        for dirpath, dirnames, filenames in os.walk(directory):
            for file in filenames:
                if file.endswith('mp3'):
                    ui.listWidget.addItem(os.path.join(dirpath, file))
             
def pause():
    global flag
    if flag:
        pygame.mixer.music.pause()
        ui.pushButton_4.setStyleSheet("background-color: red")
        flag = False
    else:
        pygame.mixer.music.unpause()
        ui.pushButton_4.setStyleSheet("background-color: None")
        flag = True
        
def stop():
    pygame.mixer.music.stop()
    
ui.pushButton.clicked.connect(open_file)
ui.pushButton_3.clicked.connect(open_folder)
ui.pushButton_2.clicked.connect(play_song)
ui.pushButton_4.clicked.connect(pause)
ui.pushButton_5.clicked.connect(stop)


sys.exit(app.exec_())