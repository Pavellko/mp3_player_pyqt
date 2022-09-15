from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pygame
import os, sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 500)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(20, 140, 311, 341))
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(80, 10, 211, 31))
        self.label.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 127);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(60, 100, 225, 23))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter)
        self.pushButton_4.setObjectName("pushButton_4")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(60, 60, 225, 23))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.splitter_3 = QtWidgets.QSplitter(Form)
        self.splitter_3.setGeometry(QtCore.QRect(300, 60, 31, 61))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(300, 30, 31, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Mp3 Folder Player"))
        self.pushButton_5.setText(_translate("Form", "Stop"))
        self.pushButton_2.setText(_translate("Form", "Play"))
        self.pushButton_4.setText(_translate("Form", "Pause"))
        self.pushButton.setText(_translate("Form", "Open File"))
        self.pushButton_3.setText(_translate("Form", "Open Folder"))
        self.pushButton_6.setText(_translate("Form", "+"))
        self.pushButton_7.setText(_translate("Form", "-"))
        self.label_2.setText(_translate("Form", "50%"))

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
                    ui.listWidget.setCurrentItem( ui.listWidget.item(i) )                       
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
    
def close_app():
    exit()  

def volum_up():
    global volume
    if volume < 0.9 :
        volume += 0.1
        ui.label_2.setText(str(round(volume*100)) +'%')
        pygame.mixer.music.set_volume(volume)     

def volum_down():
    global volume
    if volume > 0.1 :
        volume -= 0.1
        ui.label_2.setText(str(round(volume*100)) +'%')
        pygame.mixer.music.set_volume(volume)          
    

app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()
ui = Ui_Form()
ui.setupUi(Form)
Form.setWindowTitle('Mp3 Player')
Form.setFixedSize(350, 500)
Form.show()

pygame.init()
flag = False
list_song = []    
volume = 0.5
pygame.mixer.music.set_volume(volume)   
  
ui.pushButton.clicked.connect(open_file)
ui.pushButton_3.clicked.connect(open_folder)
ui.pushButton_2.clicked.connect(play_song)
ui.pushButton_4.clicked.connect(pause)
ui.pushButton_5.clicked.connect(stop)
ui.listWidget.itemDoubleClicked.connect(play_song)
ui.pushButton_6.clicked.connect(volum_up)
ui.pushButton_7.clicked.connect(volum_down)

app.lastWindowClosed.connect(close_app)
sys.exit(app.exec_())
