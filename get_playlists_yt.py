#Demo for getting a YouTube Music user's playlists

from ytmusicapi import YTMusic
import os
from dotenv import load_dotenv
load_dotenv()

yt = YTMusic("oauth.json")
#yt = YTMusic()

#User is the user's channel ID
user = 'UCOTh5gSUXmLoAvEwAcZ1QvA'

userInfo = yt.get_user('UCOTh5gSUXmLoAvEwAcZ1QvA')

# Print the list of playlists

print("Your playlists:")

for playlists in userInfo['playlists']['results']:
    # Get the tracks in the playlist
    print(playlists['title'])
    print()
    playlist = yt.get_playlist(playlists['playlistId'])
    for track in playlist['tracks']:
        print(track['title'])
