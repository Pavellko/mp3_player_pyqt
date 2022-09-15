from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pygame
import os, sys

import pafy
from youtube_dl import YoutubeDL
from mhyt import yt_download

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
    
def get_youtube():
    global link_youtube
    link_youtube = ui.lineEdit.text()
    print(link_youtube)
    ######
    # video = pafy.new(link_youtube)
    # bestaudio = video.getbestaudio()
    # bestaudio.download(f'{video.title}.mp3')
    ######
    # ydl_opts = { 'format': 'm4a/bestaudio/best', 'postprocessors': [{  'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', }]}
    # with YoutubeDL() as ydl:
    #     ydl.download([link_youtube])
    #######
    # yt_download(link_youtube, f'{video.title}.mp3' , ismusic=True, codec = "mp3")
    #######
    # video_info = YoutubeDL().extract_info( url = link_youtube, download=False )
    # filename = f"{video_info['title']}.mp3"
    # options={
    #     'format':'bestaudio/best',
    #     'keepvideo':False,
    #     'outtmpl':filename,
    #      }

    # with YoutubeDL(options) as ydl:
    #     ydl.download([video_info['webpage_url']])
    ########
    
    
    
        
    
app = QApplication(sys.argv)
ui = uic.loadUi("inter.ui")
ui.setWindowTitle('Mp3 Player')
ui.setFixedSize(350, 544)
ui.show()

pygame.init()
flag = False
list_song = []    
volume = 0.5
link_youtube = ''
pygame.mixer.music.set_volume(volume)   
  
ui.pushButton.clicked.connect(open_file)
ui.pushButton_3.clicked.connect(open_folder)
ui.pushButton_2.clicked.connect(play_song)
ui.pushButton_4.clicked.connect(pause)
ui.pushButton_5.clicked.connect(stop)
ui.listWidget.itemDoubleClicked.connect(play_song)
ui.pushButton_6.clicked.connect(volum_up)
ui.pushButton_7.clicked.connect(volum_down)
ui.pushButton_8.clicked.connect(get_youtube)

app.lastWindowClosed.connect(close_app)
sys.exit(app.exec_())
