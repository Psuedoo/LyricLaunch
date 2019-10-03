import asyncio
import string
import webbrowser
import information
import spotify
import lyricsgenius
import tkinter
import requests
from Song import Song
from spotify import User
from quart import Quart, request


REDIRECT_URI = "http://localhost:8888/callback"

global app
app = Quart(__name__)
app.spotify_client = None

class SongHandler:

    def __init__(self):
        self.oauth = spotify.OAuth2(information.SPOTIFY_CLIENT_ID, REDIRECT_URI, scope='user-read-recently-played, user-read-playback-state')
        self.genius = lyricsgenius.Genius(information.GENIUS_ACCESS_TOKEN)
        self.client = spotify.Client(information.SPOTIFY_CLIENT_ID, information.SPOTIFY_CLIENT_SECRET)
        self.lyrics = None
        self.user = None


    def run(self):
        webbrowser.open(self.oauth.url, new=0)
        app.run(port=8888)

    async def handle(self, user: User):

        # Data Received
        tracks = await user.recently_played()
        currentSong = await user.currently_playing()
        readSong = currentSong['item'].name
        readArtist = currentSong['item'].artist

        # Handle The Recieved Data
        searchResults = genius.search_song(readSong, artist = readArtist.name)
        self.lyrics = searchResults.lyrics


    # Auth
    @app.before_request
    def before_request():
        if app.spotify_client is None:
            app.spotify_client = spotify.Client(information.SPOTIFY_CLIENT_ID, information.SPOTIFY_CLIENT_SECRET)

    @app.route('/callback')
    async def hello():
        code = request.args.get('code')

        user = await User.from_code(app.spotify_client, code, redirect_uri=REDIRECT_URI, refresh=True)
        print(await SongHandler.handle(user))
        return 'Authorized!'




if __name__ == '__main__':
    webbrowser.open(SongHandler().oauth.url, new=0)
    app.run(port=8888)


