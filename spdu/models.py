from dataclasses import dataclass
from typing import List, Literal, TypedDict


class Album(TypedDict):
    track_id: str
    name: str
    artists: List[str]
    type: Literal["album", "single", "compilation"]


@dataclass
class Track:
    id: str
    isrc: str
    title: str
    artists: List[str]
    album: Album
    playlist: str
    playlist_index: int

    def get_album_artist(self):
        return self.album.artists[0]

    # def is_unique(self) -> bool:
    #     return len(self.albums) == 1

    # def add_album(self, album: Album):
    #     self.albums.append(album)


@dataclass
class Playlist:
    name: str
    tracks: List[Track]


@dataclass
class ApiTracks:
    total: int
    items: List


@dataclass
class ApiPlaylist:
    name: str
    tracks: ApiTracks
