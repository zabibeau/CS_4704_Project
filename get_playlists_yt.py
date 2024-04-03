#Demo for getting a YouTube Music user's playlists

from ytmusicapi import YTMusic
import os
from dotenv import load_dotenv
load_dotenv()

yt = YTMusic("oauth.json")

user = 'eatacrakker 1'
playlists = yt.get_user_playlists(user, yt.get_artist(user))

# Print the list of playlists
print("Your playlists:")
for playlist in playlists['items']:
    print(playlist['title'])
    # Get the tracks in the playlist
    tracks = yt.get_playlist(playlist['playlistId'], limit=100)  # Limit set to 100, adjust as necessary
    for track in tracks['tracks']:
        print(track['title'])
    print('\n')
