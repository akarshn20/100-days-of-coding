import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup


URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = "Your_client_ID"
CLIENT_SECRET = "Your_Client_Secret"

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
response = requests.get(URL + date)
top_songs = response.text
soup = BeautifulSoup(top_songs, "html.parser")
top_100 = [songs.getText().strip() for songs in soup.select(selector="li ul li h3")]

# Spotify Authentication
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="Akarsh"
    )
)
user_id = spotify.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uri = []
year = date.split("-")[0]

for song in top_100:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in spotify
playlist = spotify.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uri)



