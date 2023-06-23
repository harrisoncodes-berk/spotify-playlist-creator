from dotenv import dotenv_values
import sys
sys.path.append("./src")
import spotify

client_id = dotenv_values(".env")["CLIENT_ID"]
client_secret = dotenv_values(".env")["CLIENT_SECRET"]
redirect_uri = dotenv_values(".env")["REDIRECT_URI"]

spotify = spotify.Spotify(client_id, client_secret, redirect_uri)

playlist_id = "2gJnzk7FBZ40ZsincUKDcd"

songs = spotify.get_top_tracks("6eUKZXaKkcviH0Ku9w2n3V", 5)

spotify.add_songs_to_playlist(playlist_id, songs)