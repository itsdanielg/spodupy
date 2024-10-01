from spdu.models import ApiPlaylist, ApiTracks
from spdu.user import get_user

sp = get_user()


def extract_playlist_id(playlist_url):
    return playlist_url.split("/")[-1].split("?")[0]


def fetch_playlist(playlist_url):
    if playlist_url is None:
        return None

    playlist_id = extract_playlist_id(playlist_url)
    playlist_details = sp.playlist(playlist_id)

    results = playlist_details["tracks"]
    tracks = results["items"]
    while results["next"]:
        results = sp.next(results)
        tracks.extend(results["items"])

    return ApiPlaylist(
        name=playlist_details["name"],
        tracks=ApiTracks(
            total=len(tracks),
            items=[track["track"] for track in tracks]
        )
    )
