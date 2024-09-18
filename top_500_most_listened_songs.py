import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Spotify API credentials
CLIENT_ID = 'your_client_id'  # Replace with your client ID
CLIENT_SECRET = 'your_client_secret'  # Replace with your client secret
REDIRECT_URI = 'http://localhost:8888/callback'  # Replace with your redirect URI

# Scope required to access user's top tracks and modify playlists
SCOPE = 'user-top-read playlist-modify-public playlist-modify-private'

# Authenticate and get the access token
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=SCOPE))

# Get the current user's profile (to retrieve user ID)
user_id = sp.current_user()['id']

# Get top 500 tracks (Spotify API allows fetching top tracks in chunks of 50)
top_tracks = []
limit = 50
offset = 0

while len(top_tracks) < 500:
    results = sp.current_user_top_tracks(limit=limit, offset=offset, time_range='long_term')
    top_tracks.extend(results['items'])
    offset += limit
    if len(results['items']) == 0:
        break

# Limit to 500 tracks if necessary
top_tracks = top_tracks[:500]

# Create a new playlist for the user
playlist_name = 'Top 500 Most Listened Songs'
playlist_description = 'A playlist of my top 500 most listened songs.'
new_playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False, description=playlist_description)

# Add tracks to the newly created playlist
track_ids = [track['id'] for track in top_tracks]
for i in range(0, len(track_ids), 100):
    sp.playlist_add_items(new_playlist['id'], track_ids[i:i + 100])

print(f'Playlist "{playlist_name}" created with {len(track_ids)} tracks.')
