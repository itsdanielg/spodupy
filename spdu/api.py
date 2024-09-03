import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
from spdu.utils import extract_playlist_id

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

if not client_id or not client_secret:
    raise ValueError(
        "Missing Spotify API credentials. Please set SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET in your environment."
    )

# Set up the Spotify client using client credentials flow
auth_manager = SpotifyClientCredentials(
    client_id=client_id, client_secret=client_secret
)
sp = spotipy.Spotify(auth_manager=auth_manager)


def fetch_playlist_tracks(playlist_url):
    if playlist_url is None:
        return None

    playlist_id = extract_playlist_id(playlist_url)
    results = sp.playlist_tracks(playlist_id)
    tracks = results["items"]

    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])

    return [track["track"] for track in tracks]


def delete_playlist_tracks(playlist_url, duplicates):
    playlist_id = extract_playlist_id(playlist_url)
    track_uris = [track["uri"] for track in duplicates]
    sp.playlist_remove_all_occurrences_of_items(playlist_id, track_uris)
