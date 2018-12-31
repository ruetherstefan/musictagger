from os import listdir
import math
from shutil import copyfile

from pydub import AudioSegment
import pygame

from main.tags import Tags


class SongDirectory:

    song_ordner = "C:\P\P\musictagger\inputmusic\\"
    watched_song_index = 0

    directory_files = listdir(song_ordner)

    tags = Tags()

    def inc_watched_song_index(self):
        self.watched_song_index += 1
        self.tags = Tags()

    def get_currend_song_path(self):
        return self.song_ordner + 'playcopy' + str(self.watched_song_index) + '.mp3'

    def get_current_song_real_path(self):
        return self.song_ordner + str(self.directory_files[self.watched_song_index])

    def get_song_length(self):
        #audiofile = eyed3.load(self.get_currend_song_path())
        #return int(math.floor(audiofile.info.time_secs))
        return 42

    def save_id3(self):
        pass
#audiofile = eyed3.load(self.get_currend_song_path())
        #audiofile.tag.publisher = self.tags.create_id3()
        #audiofile.tag.save()

    def lade_lied(self):
        if self.get_current_song_real_path().endswith(".mp3"):
            copyfile(self.get_current_song_real_path(), self.get_currend_song_path())
        else:
            AudioSegment.from_wav(self.get_current_song_real_path()).export(self.get_currend_song_path(), format="mp3")

        pygame.mixer.music.load(self.get_currend_song_path())
        pygame.mixer.music.play()
