from os import listdir, remove
from shutil import copyfile

from pydub import AudioSegment
import pygame
import taglib


PLAYCOPY = 'playcopy'


class SongDirectory():

    song_ordner = "C:\P\P\musictagger\inputmusic\\"
    watched_song_index = 0

    directory_files = listdir(song_ordner)

    def inc_watched_song_index(self):
        self.watched_song_index += 1
        if self.watched_song_index == len(self.directory_files):
            self.watched_song_index = 0

    def dec_watched_song_index(self):
        self.watched_song_index -= 1
        if self.watched_song_index == -1:
            self.watched_song_index = len(self.directory_files) - 1

    def get_currend_song_path(self):
        return self.song_ordner + PLAYCOPY + str(self.watched_song_index) + '.mp3'

    def get_current_song_real_path(self):
        return self.song_ordner + self.get_current_song_name()

    def get_current_song_name(self):
        return str(self.directory_files[self.watched_song_index])

    def lade_lied(self):
        if self.get_current_song_real_path().endswith(".mp3"):
            copyfile(self.get_current_song_real_path(), self.get_currend_song_path())
        else:
            AudioSegment.from_wav(self.get_current_song_real_path()).export(self.get_currend_song_path(), format="mp3")

        pygame.mixer.music.load(self.get_currend_song_path())
        pygame.mixer.music.play()

    def delete_all_playcopys(self):
        directory_files_with_copies = listdir(self.song_ordner)

        for file in directory_files_with_copies:
            if PLAYCOPY in file:
                remove(self.song_ordner + file)

    def get_currend_song_length(self):
        song = taglib.File(self.get_current_song_real_path())
        return song.length

    def save_comment(self, tagstring):
        song = taglib.File(self.get_current_song_real_path())
        song.tags["COMMENT"] = [tagstring]
        song.save()

