# 2.	Define a class called Songs, it will show the lyrics of a song. Its __init__() method should have two arguments: self and lyrics. lyrics is a list. Inside your class create a method called sing_me_a_song that prints each element of lyrics on his own line.

class Songs:
    def __init__(self, lyrics:list):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for lyric in self.lyrics:
            print(lyric + '\n')
            
song = Songs(lyrics=['abc', 'def', 'ghi'])
song.sing_me_a_song()