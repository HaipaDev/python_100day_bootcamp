from datetime import datetime
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
from pprint import pprint

song_names = ['Yoru ni Kakeru']
#song_names = ['IDOL']
#song_names = ['夜に駆ける']
song_artists = ['YOASOBI']

user_input=datetime.strftime(datetime.now(),"%Y-%m-%d")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="ccb5dce6150440078ee92ef857036fd6",
        client_secret="46192cbee5cb4b5fa72fbfdabe0ec9c3",
        show_dialog=True,
        cache_path="token.txt",
        username="MaciejKrefft03", 
    )
)
user_id = sp.current_user()["id"]

song_uris = []
year = user_input.split("-")[0]
for song,artist in zip(song_names,song_artists):
    #result = sp.search(q=f"track:{song} artist:{artist} year:{year}", type="track")
    result = sp.search(q=f"track: {song} artist: {artist} year: {year}", type="track")
    pprint(result)
    print(f"Looking for: 'track: {song} artist: {artist} year: {year}' ( {result['tracks']['href']} )")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        print(f"Found: {result['tracks']['items'][0]['album']['artists'][0]['name']} - {result['tracks']['items'][0]['album']['name']}")
    except IndexError:
        print(f"{artist} - {song} [{year}] doesn't exist on Spotify. Skipped.")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"New playlist '{user_input} Billboard 100' successfully created on Spotify!")