import os
from flask import Flask, request, redirect, url_for
from ytmusicapi import YTMusic
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

yt = YTMusic("oauth.json")

@app.route('/')
def login():
    # Redirect user to YT authorization URL
    return

@app.route('/ytcallback')
def ytcallback():

    # Define new playlist details
    playlist_name = 'New Awesome Playlist'
    playlist_description = 'Automatically created playlist'

    playlist = yt.create_playlist(playlist_name, playlist_description)

    return f"Playlist created"

if __name__ == "__main__":
    app.run(debug=True, port=8888)