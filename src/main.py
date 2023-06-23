from dotenv import dotenv_values
import spotify

client_id = input("Enter your client id: ") or dotenv_values(".env")["CLIENT_ID"]
client_secret = (
    input("Enter your client secret: ") or dotenv_values(".env")["CLIENT_SECRET"]
)
redirect_uri = (
    input("Enter your redirect uri: ") or dotenv_values(".env")["REDIRECT_URI"]
)

spotify = spotify.Spotify(client_id, client_secret, redirect_uri)

playlist_name = input("Enter the name of the playlist: ")
playlist_description = input("Enter the description of the playlist: ")

playlist_id = spotify.create_playlist(playlist_name, playlist_description)

while True:
    artist_name = input("Enter the name of the artist: ")
    if not artist_name:
        break

    number_of_tracks = input("Enter the number of tracks: ")
    if (
        not number_of_tracks
        or not number_of_tracks.isdigit()
        or int(number_of_tracks) > 10
    ):
        number_of_tracks = 5

    artist_id = spotify.get_artist_id(artist_name)
    top_tracks = spotify.get_top_tracks(artist_id, int(number_of_tracks))

    spotify.add_songs_to_playlist(playlist_id, top_tracks)
