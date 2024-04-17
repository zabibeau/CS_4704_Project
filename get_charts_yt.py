#Demo for getting a YouTube Music user's playlists

from ytmusicapi import YTMusic
import os
from dotenv import load_dotenv
load_dotenv()

yt = YTMusic("oauth.json")

#User is the user's channel ID
user = 'UCOTh5gSUXmLoAvEwAcZ1QvA'

chart = yt.get_charts("ZZ")
# Print the list of playlists

print("Global Top 40 artists:")

for artist in chart['artists']['items']:
    print(artist['rank'] + " " + artist['title'])