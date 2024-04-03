'''
This script is a demo for how we can go about getting the playlists of a user using the Spotify API.
Obviously this is just a demo and we will need to modify this to fit our needs.
'''


import spotipy
from spotipy.oauth2 import SpotifyOAuth
import spotipy.client
import os
from dotenv import load_dotenv
load_dotenv()

# Define your client ID, client secret, and redirect URI
CLIENT_ID = os.environ['SPOTIFY_CLIENT_ID']
CLIENT_SECRET = os.environ['SPOTIFY_CLIENT_SECRET']

# This redirect URI is used for the user to grant access to the application. Just does this locally for now.
REDIRECT_URI = 'http://localhost:8888/callback'

# Define the scope of the calls we make in this script
SCOPE = 'playlist-read-private'

# Authenticate the user
sp = spotipy.client.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                        client_secret=CLIENT_SECRET,
                                                        redirect_uri=REDIRECT_URI,
                                                        scope=SCOPE))

# Retrieve the user's playlists

user = ''#put some username here
playlists = sp.user_playlists(user)

# Print the list of playlists
print("Your playlists:")
for playlist in playlists['items']:
    print(playlist['name'])
    for track in sp.playlist_tracks(playlist['id'])['items']:
        print(track['track']['name'].encode('utf-8'))
    print('\n')