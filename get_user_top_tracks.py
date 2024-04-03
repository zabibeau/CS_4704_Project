import os
from flask import Flask, request, redirect, url_for
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Spotify credentials and settings
CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIFY_REDIRECT_URI')
SCOPE = 'user-top-read'

# Create SpotifyOAuth object for handling authorization
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope=SCOPE,
                        cache_path='cache.txt',
                        open_browser=True)

print(sp_oauth.get_authorize_url())

@app.route('/')
def login():
    # Redirect user to Spotify authorization URL
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

@app.route('/callback')
def callback():
    # Retrieve authorization code from callback query parameters
    code = request.args.get('code')
    
    # Exchange authorization code for access token
    token_info = sp_oauth.get_access_token(code, as_dict=False)
    # Create Spotify client with access token
    sp = spotipy.Spotify(auth=token_info)
    
    # Define new playlist details
    
    # Create the playlist for the current user
    tracks = sp.current_user_top_tracks(time_range='short_term', limit=10)
    
    print(tracks)

    return f"Top Tracks found"
    

if __name__ == "__main__":
    app.run(debug=True, port=8888)
