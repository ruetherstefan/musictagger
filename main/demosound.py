#from kivy.core.audio import SoundLoader


#sound = SoundLoader.load('C:\P\P\musictagger\inputmusic\song.mp3')
#print(sound)
#print(sound.length)
#print("living")
#sound.play()

import pygame


file = 'C:\P\P\musictagger\inputmusic\song.mp3'
pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.mixer.music.set_pos(20)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    #print(pygame.mixer.music.get_pos())
