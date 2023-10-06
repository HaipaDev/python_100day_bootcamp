import spotipy
from spotipy.oauth2 import SpotifyOAuth
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