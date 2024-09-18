# Spotify Automation Scripts

This repository contains various Python scripts that interact with the Spotify Web API to automate tasks related to managing playlists, liking tracks, and more. These scripts use OAuth2 for authentication and leverage the `spotipy` library to interact with the Spotify API.

## Features

- **Like All Songs from Playlists You Created**: Automatically likes all the songs that are in playlists created by you.
- **Top 500 Tracks Playlist**: Generates a playlist of your top 500 most listened-to tracks.

## Prerequisites

Before running any of the scripts, ensure you have the following:

1. **Python 3.6+** installed on your system.
2. A **Spotify Developer Account**. You can sign up for free and create an app [here](https://developer.spotify.com/dashboard/applications).
3. Your **Spotify Developer App** credentials, including:
   - **Client ID**
   - **Client Secret**
   - **Redirect URI** (e.g., `http://localhost:8888/callback`)
4. Install the required Python libraries by running:
   pip install spotipy
   pip install python-dotenv

## Setup

1. Clone this repository to your local machine.
2. (Optional but recommended) Create and activate a virtual environment:
   - python -m venv venv
   - source venv/bin/activate   # On Windows: venv\Scripts\activatd
3. Set up environment variables for your Spotify API credentials by creating a .env file in the root directory with the following:
   - SPOTIPY_CLIENT_ID='your_spotify_client_id'
   - SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
   - SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'

## Scripts Overview

### 1. Like All Songs from Playlists Created by You
This script likes all songs from playlists that you have created.

To run the script:
    python like_songs_in_playlists.py

#### What the script does:

   - Authenticates the user with Spotify using OAuth2.
   - Retrieves all playlists created by the user.
   - Likes every song in those playlists by adding them to the user's "Liked Songs" collection.

### 2. Create a Playlist of Your Top 500 Most Listened Songs

This script generates a playlist containing your top 500 most listened-to tracks.

To run the script:
    python create_top_500_playlist.py

#### What the script does:

   - Authenticates the user with Spotify using OAuth2.
   - Fetches your top 500 most played tracks from Spotify.
   - Creates a new playlist and adds those tracks to it.

## API Scopes
Some scripts require specific API scopes for accessing certain Spotify data. When running a script for the first time, you'll be prompted to authorize the app based on the required permissions.

Here are some common scopes used in the scripts:

   - playlist-read-private: Allows access to read private playlists.
   - playlist-modify-public: Allows modifying public playlists.
   - user-top-read: Provides access to the user's top tracks and artists.
   - user-library-modify: Allows modifying the user's "Liked Songs."

Feel free to explore and modify the scripts to fit your needs! Contributions and feedback are always welcome.

