from bs4 import BeautifulSoup
import requests
from datetime import datetime

CATEGORY="japan-hot-100"

import os
if(os.path.exists("category.txt")):
    with open("category.txt","r") as file:
        print(file.read())
        if(len(file.read())>0):
            CATEGORY=file.read()
            
print("Which year do you want to travel to?")
user_input="-"
while(len(user_input)!=10 and len(user_input)!=0):
    user_input=input("Type the date in a format of YYYY-MM-DD (empty for current date): ")

ENDPOINT=f"https://www.billboard.com/charts/{CATEGORY}/{user_input}"
if(user_input==""):
    user_input=datetime.strftime(datetime.now(),"%Y-%m-%d")
    ENDPOINT=f"https://www.billboard.com/charts/{CATEGORY}/"
print(user_input)
print(f"Getting data from: {ENDPOINT}")
    
response=requests.get(ENDPOINT)
html_response=response.text

soup=BeautifulSoup(html_response,"html.parser")
# with open("website.html","w") as file:
#     file.write(soup.prettify())
#titles=soup.find_all(name="h3",id="title-of-a-story")
#print([title.getText() for title in titles])

#song_names_spans = soup.select("li ul li h3")
#song_author_spans = soup.select("li ul li span:first-child")
#song_author_spans = [item.find("span") for item in soup.select("li ul li")]
# song_names = [song.getText().strip() for song in song_names_spans]
# song_authors = [author.getText().strip() if author else "" for author in song_author_spans if author is not None]

song_names = []
song_artists = []
# list_items = soup.select(".chart-list-item")
list_items = soup.select(".chart-results-list li ul li")
for item in list_items:
    # Find the h3 tag (song name) and span tag (author) within the same list item
    song_name = item.find("h3")
    artist_span = item.find("span")

    # Check if both song_name and author_span are found
    if song_name and artist_span:
        song_names.append(song_name.getText().strip())
        song_artists.append(artist_span.getText().strip())


for i,song in enumerate(song_names):
    print(f"{song_artists[i]} - {song}")
    
print()
print()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials,SpotifyOAuth
# birdy_uri = 'spotify:artist:2WX2uTcsvV5OnS0inACecP'
# spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="ccb5dce6150440078ee92ef857036fd6",client_secret="46192cbee5cb4b5fa72fbfdabe0ec9c3",scope="playlist-modify-private"))

# results = spotify.artist_albums(birdy_uri, album_type='album')
# albums = results['items']
# while results['next']:
#     results = spotify.next(results)
#     albums.extend(results['items'])

# for album in albums:
#     print(album['name'])


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
found_song_names_list=[]
duplicates_checked=[]
year = user_input.split("-")[0]

from pprint import pprint
def lookup_sp_song(query):
    #result = sp.search(q=f"track:{song} artist:{artist} year:{year}", type="track")
    result = sp.search(q=query, type="track")
    #pprint(result)
    print(f"Looking for: 'track: {song} artist: {artist} year: {year}' ( {result['tracks']['href']} )")
    try:
        found_song_artist=result['tracks']['items'][0]['album']['artists'][0]['name']
        found_song_name=result['tracks']['items'][0]['album']['name']
        if(found_song_name not in found_song_names_list):
            found_song_names_list.append(found_song_name)
            if("lofi" in found_song_artist.lower() or "lofi" in found_song_name.lower()):
                return lookup_sp_song(f"{song}")
            uri = result["tracks"]["items"][0]["uri"]
            song_uris.append(uri)
            print(f"Found: {found_song_artist} - {found_song_name}")
        else:
            if(f"{artist} - {song}" not in duplicates_checked):
                print(f"Found duplicate of {found_song_artist} - {found_song_name} by searching {artist} - {song}")
                duplicates_checked.append(f"{artist} - {song}")
                return lookup_sp_song(f"{song} {artist}")

    except IndexError:
        print(f"{artist} - {song} doesn't exist on Spotify. Skipped.")
    print()


for song,artist in zip(song_names,song_artists):
    lookup_sp_song(f"track: {song} artist: {artist} year: {year}")
        
playlist = sp.user_playlist_create(user=user_id, name=f"{user_input} {CATEGORY}", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(f"New playlist '{user_input} {CATEGORY}' successfully created on Spotify!")