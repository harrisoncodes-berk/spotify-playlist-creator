import base64
import requests
import urllib.parse


def get_access_token(client_id, client_secret, redirect_uri):
    # Step 1: Obtain authorization code
    authorize_url = "https://accounts.spotify.com/authorize"
    params = {
        "response_type": "code",
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "scope": "user-read-private user-read-email playlist-read-private playlist-modify-private playlist-modify-public",  # Requested scopes
        "state": "random_state",  # Optional state parameter for security (anti-CSRF)
    }
    authorize_url_with_params = authorize_url + "?" + urllib.parse.urlencode(params)
    print(
        f"Please visit the following URL to authorize the application: {authorize_url_with_params}"
    )
    authorization_code = input("Enter the authorization code from the callback URL: ")

    # Step 2: Exchange authorization code for access token
    token_url = "https://accounts.spotify.com/api/token"
    data = {
        "grant_type": "authorization_code",
        "code": authorization_code,
        "redirect_uri": redirect_uri,
    }
    headers = {
        "Authorization": f'Basic {base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()}'
    }
    response = requests.post(token_url, data=data, headers=headers)

    # Step 3: Handle the response
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Token exchange failed with status code:", response.status_code)
        return None
