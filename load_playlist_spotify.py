import requests
from urllib.parse import urlencode
import base64
import webbrowser
import os
from dotenv import load_dotenv
from flask import Flask, request  
import time

app = Flask(__name__)

load_dotenv()

# Define Spotify app credentials
client_id = os.environ['SPOTIFY_CLIENT_ID']
client_secret = os.environ['SPOTIFY_CLIENT_SECRET']
redirect_uri = os.environ['SPOTIFY_REDIRECT_URI']  # Your redirect URI

auth_headers = {
    "client_id": client_id,
    "client_secret": client_secret,
    "response_type": "code",
    "redirect_uri": redirect_uri,
    "scope": "playlist-modify-public playlist-modify-private"
}

# Global variable to store the authorization code
authorization_code = None

def wait_for_authorization_code():
    global authorization_code
    while authorization_code is None:
        time.sleep(0.1)  # Wait for 1 second before checking again
        if authorization_code is not None:
            break
    return authorization_code

@app.route('/callback')
def callback():
    global authorization_code
    full_url = request.url
    authorization_code = full_url.split('code=')[1]
    return 'Authorization code received successfully. You may now close this tab.'

# Open Spotify authorization page
webbrowser.open("https://accounts.spotify.com/authorize?" + urlencode(auth_headers))

# Start the Flask application
app.run(port=8888)

# Wait until authorization code is received
authorization_code = wait_for_authorization_code()

# Proceed with further actions using the authorization code
encoded_credentials = (base64.b64encode(client_id.encode() + b':' + client_secret.encode())).decode('utf-8')

token_headers = {
    "Authorization": f"Basic {encoded_credentials}",
    "Content-Type": "application/x-www-form-urlencoded"
}

token_data = {
    'grant_type': 'authorization_code',
    'code': authorization_code,
    'redirect_uri': redirect_uri
}
response = requests.post("https://accounts.spotify.com/api/token", headers=token_headers, data=token_data)
print(response.json())


token = response.json()['access_token']

user = 'bubby000'

# Create a playlist for the user
playlist_headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

playlist_data = {
    "name": "My New Playlist # 2",
    "public": False,
    "description": "My new playlist description"
}

resp = requests.post(f"https://api.spotify.com/v1/users/{user}/playlists", headers=playlist_headers, json=playlist_data)
# Stop the Flask application
print(resp.json())

# Close the Flask application
exit(0)