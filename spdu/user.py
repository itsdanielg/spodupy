import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


def get_user():

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

    return sp
