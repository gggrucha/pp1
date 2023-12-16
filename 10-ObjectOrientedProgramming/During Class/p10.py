'''
10.	Create a class that represents pieces of music. 
Define a class constructor that allows you to set the initial values of the music piece 
(artist, track title, album, year) when the object is created. 
Complete the class with the __str__ method returning the song data as a string, in the format as below (4 lines). 
Then, create two objects that represent two different pieces of music. Display these objects. 
Sample result:
Performer: Ed Sheeran
Song:      Hearts Don't Break Around Here
Album:     Divide
Year:      2017

…
…
…
…
'''
class Pieces():
    def __init__(self, artist, track_title, album, year):
        self.artist = artist
        self.track_title = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return f'Performer: {self.artist}\nSong:      {self.track_title}\nAlbum:     {self.album}\nYear:      {self.year}'
    

p1 = Pieces('g','f','z',2000)
print(p1)
