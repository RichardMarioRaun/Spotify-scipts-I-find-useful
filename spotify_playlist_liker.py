import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Spotify API credentials from .env
CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

# Scope required to access user's playlists and liked songs
SCOPE = 'playlist-read-private user-library-modify user-top-read playlist-modify-public'

# Authenticate and get the access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Get current user's playlists
playlists = sp.current_user_playlists()


# Iterate through each playlist
for playlist in playlists['items']:
    # Check if the playlist is created by the current user
    if playlist['owner']['id'] == sp.current_user()['id']:
        print(f"Processing playlist: {playlist['name']}")
        # Get the tracks in the playlist
        results = sp.playlist_tracks(playlist['id'])
        tracks = results['items']

        # Like each track in the playlist
        for track in tracks:
            track_id = track['track']['id']
            if track_id:
                print(f"Liking track: {track['track']['name']} by {track['track']['artists'][0]['name']}")
                sp.current_user_saved_tracks_add([track_id])

print("All tracks have been liked.")
