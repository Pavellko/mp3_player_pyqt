import pygame
# import os

pygame.mixer.init()

# list_song = []

# def open_folder():
#     global list_song
#     dir = 'C:\\Users\\pavel\\Music\\Рингтоны'

#     for dirpath, dirnames, filenames in os.walk(dir):
#         for file in filenames:
#             if file.endswith('mp3'):
#                 list_song.append(os.path.join(dirpath, file))
        
        
# open_folder()        
        
        
# for i in list_song:
#     print(i)
    
pygame.mixer.init()
pygame.mixer.music.load(r"C:\Users\pavel\Music\Рингтоны\8-bit Coffin Dance.mp3")
pygame.mixer.music.play()

pygame.quit()
             