from os import listdir
import math

import eyed3

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
        return self.song_ordner + 'currentsong.mp3'

    def get_current_song_real_path(self):
        return self.song_ordner + str(self.directory_files[self.watched_song_index])

    def get_song_length(self):
        audiofile = eyed3.load(self.get_currend_song_path())
        return int(math.floor(audiofile.info.time_secs))

    def save_id3(self):
        audiofile = eyed3.load(self.get_currend_song_path())
        audiofile.tag.publisher = self.tags.create_id3()
        audiofile.tag.save()
