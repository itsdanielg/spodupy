import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from tqdm import tqdm
from spdu.utils import extract_playlist_id, get_colored_str

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
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv('SPOTIPY_CLIENT_ID'),
    client_secret=os.getenv('SPOTIPY_CLIENT_SECRET'),
    redirect_uri=os.getenv('SPOTIPY_REDIRECT_URI'),
    scope=os.getenv('SPOTIPY_SCOPE')
))


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
    track_ids = []

    # Collect track IDs from playlist 2 duplicates
    for track in duplicates:
        # Collect IDs from playlist 2 albums
        for album in track['playlist_two_albums']:
            if 'id' in album:
                track_ids.append(album['id'])

    # If there are no tracks to delete, exit the function
    if not track_ids:
        print("No tracks to delete.")
        return

    # Initialize the progress bar
    with tqdm(total=len(track_ids), desc="Deleting tracks", unit="track") as pbar:
        successful_deletions = 0
        for track_id in track_ids:
            try:
                # Attempt to remove the track
                sp.playlist_remove_all_occurrences_of_items(
                    playlist_id, [track_id])
                successful_deletions += 1
            except Exception as e:
                # Print error message in red if an exception occurs
                print(get_colored_str(
                    f"Error deleting track with ID {track_id}: {e}", "red"))
            finally:
                # Update the progress bar regardless of success or failure
                pbar.update(1)

    # Print success message in green if there were successful deletions
    if successful_deletions == 0:
        print(get_colored_str("No tracks were deleted.", "red"))
    elif successful_deletions != len(track_ids):
        print(get_colored_str(
            f"Error deleting track with ID {track_id}: {e}", "yellow"))
    else:
        print(get_colored_str(f"Successfully deleted {
              successful_deletions} tracks from the playlist.", "green"))
