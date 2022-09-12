from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pygame import mixer

app = QApplication([])
ui = uic.loadUi("inter.ui")

ui.setWindowTitle('Mp3 Player')
ui.setFixedSize(350, 500)
ui.show()

def open_file():
    file_name = QFileDialog()
    file_name.setFileMode(QFileDialog.ExistingFiles)
    names = file_name.getOpenFileNames()
    song = names[0]
    ui.listWidget.addItems(song)

def play_song():
    path = ui.listWidget.currentItem().text()
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

ui.pushButton.clicked.connect(open_file)
ui.pushButton_2.clicked.connect(play_song)

app.exec_()