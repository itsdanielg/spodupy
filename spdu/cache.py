from dataclasses import asdict
import os
import json
import time

from spdu.api import extract_playlist_id, fetch_playlist
from spdu.models import ApiPlaylist, ApiTracks, Track

EXPIRATION = 3600


def read_json_file(file_path) -> ApiPlaylist:
    with open(file_path, 'r') as file:
        api_playlist = json.load(file)
        return ApiPlaylist(
            name=api_playlist["name"],
            tracks=ApiTracks(
                total=api_playlist["tracks"]["total"],
                items=api_playlist["tracks"]["items"]
            )
        )


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(asdict(data), file)


def get_playlist(playlist_url, reset_cache=False) -> ApiPlaylist:
    if playlist_url is None:
        return

    playlist_id = extract_playlist_id(playlist_url)
    FILE_PATH = f'{playlist_id}.json'

    if reset_cache:
        data = fetch_playlist(playlist_url)
        write_json_file(FILE_PATH, data)
        return data

    if os.path.exists(FILE_PATH):
        # Check if the file is expired
        file_mod_time = os.path.getmtime(FILE_PATH)
        if time.time() - file_mod_time < EXPIRATION:
            # File is still valid, read from it
            return read_json_file(FILE_PATH)

    # File does not exist or is expired, fetch from API
    data = fetch_playlist(playlist_url)
    write_json_file(FILE_PATH, data)
    return data
