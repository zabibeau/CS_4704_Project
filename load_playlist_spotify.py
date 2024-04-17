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
SCOPE = 'user-read-private,user-read-email,playlist-modify-public,playlist-modify-private'

# Create SpotifyOAuth object for handling authorization
sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope=SCOPE)

@app.route('/')
def login():
    # Redirect user to Spotify authorization URL
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

def search_tracks(sp, track_queries):
    """Search for tracks by name and artist, and return their URIs."""
    track_uris = []
    for query in track_queries:
        result = sp.search(q=query, limit=1, type='track')
        tracks = result['tracks']['items']
        if tracks:
            track_uris.append(tracks[0]['uri'])
    return track_uris

def add_tracks_to_playlist(sp, playlist_id, track_uris):
    """Add tracks to a specific playlist."""
    sp.playlist_add_items(playlist_id=playlist_id, items=track_uris)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code, as_dict=False, check_cache=False)
    sp = spotipy.Spotify(auth=token_info)
    user_id = sp.current_user()['id']
    
    # Create the playlist
    playlist_name = 'New Awesome Playlist'
    playlist_description = 'Automatically created playlist featuring Gunna'
    playlist = sp.user_playlist_create(user=user_id, name=playlist_name, description=playlist_description, public=True)
    playlist_id = playlist['id']

    # Tracks by Gunna to be added to the playlist
    track_queries = ['Drip Too Hard - Gunna', 'Skybox - Gunna', 'Wunna - Gunna']
    track_uris = search_tracks(sp, track_queries)
    add_tracks_to_playlist(sp, playlist_id, track_uris)

    return f"Playlist created and tracks added: {playlist['external_urls']['spotify']}"

if __name__ == "__main__":
    app.secret_key = 'your_secret_key_here'  # Ensure you set this in your environment variables
    app.run(debug=True, port=8888)
