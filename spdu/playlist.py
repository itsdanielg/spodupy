from typing import List
from spdu.models import Album, ApiPlaylist, Playlist, Track


def get_track_identifier(identifier: str, track: Track):
    if identifier == "id":
        return track.id
    return track.isrc


def init_playlist(api_playlist: ApiPlaylist) -> Playlist:
    if api_playlist is None:
        return

    tracks = []
    for i, track in enumerate(api_playlist.tracks.items):
        track_details = Track(
            id=track['id'],
            isrc=track['external_ids'].get('isrc'),
            title=track['name'],
            artists=[artist['name'] for artist in track['artists']],
            album=Album(
                track_id=track['id'],
                name=track['album']['name'],
                artists=[artist['name']
                         for artist in track['album']['artists']],
                type=track['album']['album_type']
            ),
            playlist_index=i+1,
            playlist=api_playlist.name
        )
        tracks.append(track_details)

    return Playlist(
        name=api_playlist.name,
        tracks=tracks
    )


def process_playlist(tracks_dict: dict[str, Track], playlist: Playlist, identifier: str) -> None:
    if playlist is None:
        return

    for track in playlist.tracks:
        track_identifier = get_track_identifier(identifier, track)
        if track_identifier not in tracks_dict:
            tracks_dict[track_identifier] = []

        tracks_dict[track_identifier].append(track)
