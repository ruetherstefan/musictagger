from os import listdir
import os


import eyed3

#Demo files
directory_files = listdir("C:\P\P\musictagger\inputmusic")
print(directory_files)

#Demo GUI


#Demo Play Song


#Demo tagging
#audiofile = eyed3.load("C:\P\P\musictagger\inputmusic\song.mp3")
#print(str(directory_files[0]))   --------- Renaming needed
file = "C:\P\P\musictagger\inputmusic\\" + str(directory_files[1])

os.rename(file, file + "b")
os.rename(file + "b", file)
os.rename(file, file + "b")
os.rename(file + "b", file)

#print(file)

#audiofile = eyed3.load(file)

#print(audiofile.tag.publisher)

#audiofile.tag.save()

