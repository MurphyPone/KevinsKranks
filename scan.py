import eyed3 # lets us fetch mp3 metadata
import os

# path = input("Input the path to your music library \n it should look somethign like this")
# song = eyed3.load("03 - Boyz 2 Menace ft Gudda Gudda (DatPiff Exclusive).mp3")
my_path = "/Users/petermurphy/github/KevinsKranks/Lil Wayne - Dedication 6 (DatPiff.com)"
album = sorted(os.listdir(my_path))

for f in album:
    if(f.endswith(".mp3")):
        song = eyed3.load(my_path+"/"+f)
        #print(dir(song.tag))
        print(song.tag.album)
        print(song.tag.artist)
        print(song.tag.album_artist)
        print(song.tag.title)
        print(song.tag.genre)
        #print(song.tag.year)
        print("\n")
