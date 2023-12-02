from bs4 import BeautifulSoup
from dotenv import load_dotenv
import requests,spotipy, os
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

Client_id = os.getenv("SPOTIPY_CLIENT_ID")
Client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
Username = os.getenv("SPOTIPY_USERNAME")

# scrapping billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, "html.parser")
song_names_spans = soup.select("li ul li h3")
song_names = [song.getText().strip() for song in song_names_spans]

# spotify authentication
sp = spotipy.Spotify(
    auth_manager= SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=Client_id,
        client_secret=Client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username=Username,

    )
)
user_id = sp.current_user()["id"]
print(user_id)

# searching spotify for song by title
song_uri = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    tracks = result.get("tracks", {}).get("items", [])  # Extract tracks list from the result
    if tracks:
        uri = tracks[0]["uri"]
        song_uri.append(uri)
    else:
        print(f"{song} doesn't exist in Spotify. Skipped")


#creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# adding songs found into the new playlist
try:
    sp.playlist_add_items(playlist_id=playlist["id"], items=song_uri)
    print("Songs added to the playlist successfully.")
except Exception as e:
    print("Error adding songs to the playlist:", e)