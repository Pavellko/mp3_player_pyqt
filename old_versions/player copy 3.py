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
    print(path)
    print(ind)
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play(1)
    ui.pushButton_4.setStyleSheet("background-color: None")
    flag = True
    
    
    for num, song in enumerate(list_song):
        if num == ind:        
            print(num, '-', song)
        pygame.mixer.music.queue(list_song[num])


# def next_song(ind):
#     ind += 1
#     ns = ui.listWidget.item(ind).text()
#     pygame.mixer.music.load(ns)
#     pygame.mixer.music.play()

         
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