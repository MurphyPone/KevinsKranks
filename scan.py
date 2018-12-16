import eyed3 # lets us fetch mp3 metadata

# path = input("Input the path to your music library \n it should look somethign like this")
song = eyed3.load("03 - Boyz 2 Menace ft Gudda Gudda (DatPiff Exclusive).mp3")
print(song.tag.artist)
print(song.tag.title)
