from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pygame import mixer
import os

app = QApplication([])
ui = uic.loadUi("inter.ui")

ui.setWindowTitle('Mp3 Player')
ui.setFixedSize(350, 500)
ui.show()

flag = False

def open_file():
    file_name = QFileDialog()
    file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNames()
    song = names[0]
    ui.listWidget.addItems(song)

def play_song():
    global flag
    path = ui.listWidget.currentItem().text()
    ind = ui.listWidget.currentRow()
    print(ind)
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()
    ui.pushButton_4.setStyleSheet("background-color: None")
    flag = True
    next_song(ind)
    
def next_song(ind):
    print(ui.listWidget.item(ind+1).text())
    pass
        
    
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
        mixer.music.pause()
        ui.pushButton_4.setStyleSheet("background-color: red")
        flag = False
    else:
        mixer.music.unpause()
        ui.pushButton_4.setStyleSheet("background-color: None")
        flag = True
        
def stop():
    mixer.music.stop()
    
ui.pushButton.clicked.connect(open_file)
ui.pushButton_3.clicked.connect(open_folder)
ui.pushButton_2.clicked.connect(play_song)
ui.pushButton_4.clicked.connect(pause)
ui.pushButton_5.clicked.connect(stop)

app.exec_()