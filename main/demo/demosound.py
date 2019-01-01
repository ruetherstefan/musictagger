#from kivy.core.audio import SoundLoader


#sound = SoundLoader.load('C:\P\P\musictagger\inputmusic\song.mp3')
#print(sound)
#print(sound.length)
#print("living")
#sound.play()

import pygame

from pydub import AudioSegment


file_wav = 'C:\P\P\musictagger\inputmusic\Ring03.wav'
AudioSegment.from_wav(file_wav).export('C:\P\P\musictagger\inputmusic\Ring03.mp3', format="mp3")

file = 'C:\P\P\musictagger\inputmusic\Ring03.mp3'

pygame.mixer.init()
pygame.mixer.music.load(file)
pygame.mixer.music.play()
pygame.mixer.music.set_pos(1) # not available vor wav

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
    #print(pygame.mixer.music.get_pos())
