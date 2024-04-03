from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#Searches for a song on YouTube Music using ytmusicapi.
#If a match is found, it prints the song's name and artist from YouTube Music.
#It then searches for the same song on Spotify using spotipy.
#If a match is found on Spotify, it prints the song's name, artist, and a URL to the song on Spotify.

def find_song_on_spotify(song_name):
    # YouTube Music setup
    ytmusic = YTMusic()
    
    # Search for the song on YouTube Music
    search_results = ytmusic.search(song_name)
    if not search_results:
        print("No results found on YouTube Music.")
        return
    
    # Assuming the first search result is the correct one
    song_info = search_results[0]
    print(f"Found on YouTube Music: {song_info['title']} by {song_info['artists'][0]['name']}")

    # Spotify setup
    client_id = 'your_spotify_client_id'
    client_secret = 'your_spotify_client_secret'
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    # Search for the song on Spotify
    query = f"{song_info['title']} {song_info['artists'][0]['name']}"
    results = sp.search(q=query, type='track')
    if not results['tracks']['items']:
        print("No results found on Spotify.")
        return
    
    # Assuming the first search result is the correct one
    spotify_track = results['tracks']['items'][0]
    print(f"Found on Spotify: {spotify_track['name']} by {spotify_track['artists'][0]['name']}")
    print(f"Spotify URL: {spotify_track['external_urls']['spotify']}")

# Example usage
if __name__ == "__main__":
    song_name = "Enter song name here"
    find_song_on_spotify(song_name)
