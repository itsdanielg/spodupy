import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

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


def get_playlist_tracks(playlist_url):
    playlist_id = extract_playlist_id(playlist_url)
    results = sp.playlist_tracks(playlist_id)
    tracks = results["items"]

    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])

    return [track["track"] for track in tracks]


def extract_playlist_id(playlist_url):
    return playlist_url.split("/")[-1].split("?")[0]


def find_and_print_duplicates(playlist1_tracks, playlist2_tracks, output_file=None):
    # Logic for finding duplicates and printing them
    ...


def find_and_print_duplicates_within_playlist(playlist_tracks, output_file=None):
    # Logic for finding duplicates within a single playlist
    ...


def remove_duplicate_tracks(playlist_url, duplicates):
    playlist_id = extract_playlist_id(playlist_url)
    track_uris = [track["uri"] for track in duplicates]
    sp.playlist_remove_all_occurrences_of_items(playlist_id, track_uris)
