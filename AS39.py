import random
playlist = [
    ["Hello","Someone Like You","Rolling In The Deep","Skyfall","All I Ask","Set Fire To The Rain","Water Under The Bridge","Love In The Dark","Daydreamer","Take It All"],
    ["Sparkle", "Zenzenzense","Nandemonaiya","Grand Escape","Is There Still Anything That Love Can Do?", "Dream Lantern","Katawaredoki","Cocoronaca","We'll Be Alright","Celebration"],
    ["Still Into You","Misery Business","Decode","The Only Exception","Hard Times","Ain't It Fun","Brick by Boring Brick","Ignorance","Last Hope","The Only Exception"],
    ["Helena","Na Na Na","I'm Not Okay","Welcome To The Black Parade","Teenagers","Famous Last Words","I Don't Love You","Cancer","Disenchanted","Dead!"],
    ["High Hopes","I Write Sins Not Tragedies","This Is Gospel","Emperor's New Clothes","Victorious","The Ballad of Mona Lisa","Say Amen","LA Devotee","Girls/Girls/Boys","Crazy = Genius"]
    ]
duplicateplaylist = playlist
artists = ["Adele", "Radwimps","Paramore","MCR","Panic! At The Disco"]
oldchoice1 = "name"
oldchoice2 = "name"
while True:
    if duplicateplaylist == []:
        break
    else:
        artist = random.choice(artists)
        if (artist != oldchoice1) and (artist != oldchoice2):
            oldchoice2 = oldchoice1
            oldchoice1 = artist
            artistnum = artists.index(artist)
            song = random.choice(duplicateplaylist[artistnum])
            songindex = duplicateplaylist[artistnum].index(song)
            print(artist,song)
            duplicateplaylist.pop(artistnum)
            if duplicateplaylist[artistnum] == []:
                artists.remove(artistnum)
                duplicateplaylist.pop(artistnum)