from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pygame
import os

app = QApplication([])
ui = uic.loadUi("inter.ui")

ui.setWindowTitle('Mp3 Player')
ui.setFixedSize(350, 500)
ui.show()

pygame.init()

flag = False

def open_file():
    file_name = QFileDialog()
    file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNames()
    song = names[0]
    ui.listWidget.addItems(song)

def play_song():
    song_end = False
    global flag
    path = ui.listWidget.currentItem().text()
    ind = ui.listWidget.currentRow()
    print(ind)
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    ui.pushButton_4.setStyleSheet("background-color: None")
    flag = True
    MUSIC_END = pygame.USEREVENT+1
    pygame.mixer.music.set_endevent(MUSIC_END)
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            song_end = True
    if song_end:
        print('next')
        next_song(ind)

def next_song(ind):
    song_end = False
    ns = ui.listWidget.item(ind+1).text()
    pygame.mixer.music.load(ns)
    pygame.mixer.music.play()
    MUSIC_END = pygame.USEREVENT+1
    pygame.mixer.music.set_endevent(MUSIC_END)
    for event in pygame.event.get():
        if event.type == MUSIC_END:
            song_end = True
    if song_end:
        print('next')
        next_song(ind)
     
     
          
def open_folder():
    directory = QFileDialog.getExistingDirectory()
    print(directory)
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

app.exec_()