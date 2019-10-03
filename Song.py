BASE = 'https://genius.com/'

class Song:
    def __init__(self, artist, songName):
        self.artist = artist
        self.songName = songName


    def getArtist(self):
        return self.formatArtistName()

    def setArtist(self, newArtist):
        self.artist = newArtist

    def getSongName(self):
        return self.formatSongName()

    def setSongName(self, newSongName):
        self.songName = newSongName

    def URL(self):
        return self.formatURL()

    def formatSongName(self):
        '''
        if self.songName.find("'"):
            self.songName = self.songName.replace("'", "")

        if self.songName.find('.'):
            self.songName = self.songName.replace('.', '')

        if self.songName.find('$'):
            self.songName = self.songName.replace('$', 's')

        if self.songName.find('(') or self.songName.find(')'):
            opening = self.songName.find('(')
            closing = self.songName.find(')')

            sObject = slice(opening, closing + 1)
            self.songName = self.songName.replace(self.songName[sObject], "")

        if self.songName.find('/'):
            self.songName = self.songName.replace('/', '')

        if self.songName.find('-'):
            self.songName = self.songName.replace('-','')

        if self.songName.find('&'):
            self.songName = self.songName.replace('&', '')
            '''

        return self.songName

    def formatArtistName(self):
        artists = self.artist
        firstArtist = str(artists[0])
            # return '-'.join(self.artist[0].split())
        return firstArtist

    def formatURL(self):
        formattedString = f"{BASE}{self.formatArtistName()}-{self.formatSongName()}-lyrics"
        return str(formattedString)

    def __str__(self):
        return str(f"Song Name: {self.getSongName()}\nArtist: {self.getArtist()}\nURL: {self.URL()}")
