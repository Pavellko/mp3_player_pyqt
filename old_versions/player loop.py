from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pygame
import os
import time

app = QApplication([])
ui = uic.loadUi("inter.ui")

ui.setWindowTitle('Mp3 Player')
ui.setFixedSize(350, 500)
ui.show()

pygame.init()

flag = False
list_song = []

def open_file():
    global list_song
    file_name = QFileDialog()
    file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNames()
    song = names[0]
    ui.listWidget.addItems(song)

def play_song():
    global flag, list_song
    path = ui.listWidget.currentItem().text()
    ind = ui.listWidget.currentRow()
    ui.pushButton_4.setStyleSheet("background-color: None")
    flag = True
    dlina = len(list_song)
    list_song = []
    for i in range(ind , dlina):
        list_song.append(ui.listWidget.item(i).text())
        print(ui.listWidget.item(i).text())
    print(len(list_song))
    i = 0
    pygame.mixer.music.load ( list_song[i] )
    try:
        pygame.mixer.music.queue ( list_song[i+1] ) # Queue the 2nd song
    except:
        pass
    pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
    pygame.mixer.music.play()           # Play the music

    running = True
    while running:
        for event in pygame.event.get():        
            if event.type == pygame.USEREVENT:      # A track has ended
                if len ( list_song ) - i > 1:
                    i+=1      # If there are more tracks in the queue...
                    pygame.mixer.music.queue ( list_song[i] )
 
    
    
    
    
         
def open_folder():
    global list_song
    directory = QFileDialog.getExistingDirectory()
    print(directory)
    if directory:
        for dirpath, dirnames, filenames in os.walk(directory):
            for file in filenames:
                if file.endswith('mp3'):
                    ui.listWidget.addItem(os.path.join(dirpath, file))
                    list_song.append(os.path.join(dirpath, file))

             
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

app.exec_()