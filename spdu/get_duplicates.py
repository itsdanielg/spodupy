from spdu.models import Track
from spdu.playlist import init_playlist, process_playlist


def get_duplicate_or_unique_tracks(tracks_dict, is_unique=False):
    tracks = []

    for identifier, items in tracks_dict.items():
        if is_unique and len(items) <= 1:
            tracks.append(items)
        elif not is_unique and len(items) > 1:
            tracks.append(items)

    return tracks


def get_all_duplicate_or_unique_tracks(api_playlist_one, api_playlist_two=None, is_unique=False):
    playlist_one = init_playlist(api_playlist_one)
    playlist_two = init_playlist(api_playlist_two)

    tracks_dict_id: dict[str, Track] = {}
    process_playlist(tracks_dict_id, playlist_one, "id")
    process_playlist(tracks_dict_id, playlist_two, "id")
    tracks_by_id = get_duplicate_or_unique_tracks(
        tracks_dict_id, is_unique=is_unique)

    tracks_dict_isrc: dict[str, Track] = {}
    process_playlist(tracks_dict_isrc, playlist_one, "isrc")
    process_playlist(tracks_dict_isrc, playlist_two, "isrc")
    tracks_by_isrc = get_duplicate_or_unique_tracks(
        tracks_dict_isrc, is_unique=is_unique)

    return [tracks_by_id, tracks_by_isrc]
