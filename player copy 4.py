import pygame
import os

playlist  = []

def open_folder():
    global playlist 
    dir = r'C:\Users\pavel\Music\Test'

    for dirpath, dirnames, filenames in os.walk(dir):
        for file in filenames:
            if file.endswith('mp3'):
                playlist.append(os.path.join(dirpath, file))
                print(os.path.join(dirpath, file))
                
open_folder()        
        
pygame.mixer.init()
pygame.display.init()

screen = pygame.display.set_mode ( ( 420 , 240 ) )

i = 0
pygame.mixer.music.load ( playlist[i] )  # Get the first track from the playlist

i += 1
pygame.mixer.music.queue ( playlist[i] ) # Queue the 2nd song

pygame.mixer.music.set_endevent ( pygame.USEREVENT )    # Setup the end track event
pygame.mixer.music.play()           # Play the music

running = True
while running:
    for event in pygame.event.get():        
        print(i)
        if event.type == pygame.USEREVENT:      # A track has ended
            if len ( playlist ) - i > 1: 
                i+=1      # If there are more tracks in the queue...
                pygame.mixer.music.queue ( playlist[i] )          
             
             