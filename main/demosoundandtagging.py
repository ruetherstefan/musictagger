from os import listdir
from shutil import copyfile


song_ordner = "C:\P\P\musictagger\inputmusic\\"

directory_files = listdir(song_ordner)


copyfile(song_ordner + directory_files[0], song_ordner + "playcopy0.mp3")
copyfile(song_ordner + directory_files[1], song_ordner + "playcopy1.mp3")

#play

#delete
