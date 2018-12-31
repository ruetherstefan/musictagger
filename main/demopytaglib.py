import taglib

song_ordner = "C:\P\P\musictagger\inputmusic\\"


mp3 = taglib.File(song_ordner + "01 Da Tweekaz - Jägermeister.mp3")
#wav = taglib.File(song_ordner + "song.wav")

#songs = [mp3, wav]

#for song in songs:
#    song.tags["COMMENT"] = ['#euphoric#']
#    song.save()

#mp3.tags["COMMENT"] = ['euphorickarneval']
#wav.tags["COMMENT"] = ['euphorickarnevalklassik']

#mp3.save()
#wav.save()

print(mp3.tags)
#print(wav.tags)

#song.tags["GENRE"] = ["Vocal", "Classical"]
#>>> song.save()