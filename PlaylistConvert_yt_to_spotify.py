from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyOAuth

#Extracting a song from a YouTube Music playlist.
#Searching for the song on Spotify.
#Adding the song to a Spotify playlist.

def add_song_from_youtube_to_spotify(youtube_playlist_id, spotify_playlist_id, song_index=0):
    # Initialize YTMusic
    ytmusic = YTMusic()

    # Get songs from a YouTube Music playlist
    playlist_tracks = ytmusic.get_playlist(playlistId=youtube_playlist_id, limit=1)
    if not playlist_tracks['tracks']:
        print("The YouTube Music playlist is empty or does not exist.")
        return

    # Extracting a specific song based on provided index
    song = playlist_tracks['tracks'][song_index]
    song_name = song['title']
    song_artist = song['artists'][0]['name']
    print(f"Extracted from YouTube Music: '{song_name}' by '{song_artist}'")

    # Initialize Spotipy
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="playlist-modify-public"))

    # Search for the song on Spotify
    query = f"{song_name} {song_artist}"
    results = sp.search(q=query, type='track', limit=1)
    if not results['tracks']['items']:
        print(f"No results found on Spotify for '{song_name}' by '{song_artist}'.")
        return

    spotify_track_id = results['tracks']['items'][0]['id']
    print(f"Found on Spotify, track ID: {spotify_track_id}")

    # Add the song to a Spotify playlist
    sp.playlist_add_items(playlist_id=spotify_playlist_id, items=[spotify_track_id])
    print(f"Added '{song_name}' by '{song_artist}' to the Spotify playlist.")

# Example usage
if __name__ == "__main__":
    youtube_playlist_id = 'YOUR_YOUTUBE_PLAYLIST_ID'
    spotify_playlist_id = 'YOUR_SPOTIFY_PLAYLIST_ID'
    add_song_from_youtube_to_spotify(youtube_playlist_id, spotify_playlist_id, song_index=0)
