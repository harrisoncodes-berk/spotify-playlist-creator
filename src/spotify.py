import requests
import json
import auth


class Spotify:
    def __init__(self, client_id, client_secret, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.access_token = self.get_access_token()
        print(self.access_token)
        self.user_id = self.get_user_id()
        print(self.user_id)

    def get_access_token(self):
        return auth.get_access_token(self.client_id, self.client_secret, self.redirect_uri)
    
    def get_user_id(self):
        url = "https://api.spotify.com/v1/me"
        headers = {"Authorization": f"Bearer {self.access_token}"}

        response = requests.get(url, headers=headers)
        return response.json()["id"]

    def create_playlist(self, playlist_name, description):
        url = f"https://api.spotify.com/v1/users/{self.user_id}/playlists"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        data = {
            "name": playlist_name,
            "description": description,
            "public": False,
        }

        response = requests.post(url, headers=headers, data=json.dumps(data))
        return response.json()
    
    def add_songs_to_playlist(self, playlist_id, song_uris):
        url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        data = {"uris": song_uris}

        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(response)
        print(response.json())
        return response.json()

    def get_artist_id(self, artist_name):
        url = "https://api.spotify.com/v1/search"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {"q": artist_name, "type": "artist", "limit": 1}

        response = requests.get(url, headers=headers, params=params)
        return response.json()["artists"]["items"][0]["id"]

    def get_top_tracks(self, artist_id, limit=5):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks"
        headers = {"Authorization": f"Bearer {self.access_token}"}
        params = {"market": "US"}

        response_data = requests.get(url, headers=headers, params=params).json()

        track_ids = []
        while limit > 0:
            track_ids.append(response_data["tracks"][limit]["uri"])
            limit -= 1
        return track_ids
