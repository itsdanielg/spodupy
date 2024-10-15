from typing import List
from spdu.models import Track


class PrintColor:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def get_colored_text(text: str, color: PrintColor = PrintColor.RESET):
    return f"{color}{text}{PrintColor.RESET}"


def print_color(text: str, color: PrintColor = PrintColor.RESET):
    print(get_colored_text(text, color))


def get_bold_text(text: str):
    return f"{PrintColor.BOLD}{text}{PrintColor.RESET}"


def get_colored_album(album_name, album_type):
    colors = {
        'album': PrintColor.GREEN,
        'single': PrintColor.BLUE,
        'compilation': PrintColor.YELLOW,
    }
    color = colors.get(album_type, PrintColor.RESET)
    return get_colored_text(album_name, color)


def get_artists(track: Track):
    bold_main_artist = get_bold_text(track.artists[0])
    if len(track.artists) == 1:
        return bold_main_artist
    return ", ".join([bold_main_artist] + track.artists[1:])


def print_track(track: Track):
    artists = get_artists(track)
    album = get_colored_album(track.album["name"], track.album["type"])
    print(f'{track.playlist_index}.\t{
          artists} - {track.title} ({album}) [{track.playlist}]')


def print_duplicates(duplicates: List[List[Track]]):
    print_color(color=PrintColor.GREEN,
                text=f'Total Tracks Found: {len(duplicates)}')

    for duplicate in duplicates:
        print("")
        for track in duplicate:
            print_track(track)


def print_duplicates_to_output(duplicates, output):
    with open(output, 'w') as f:
        f.write(f"\nTotal Tracks Found: {len(duplicates)}\n\n")

        for i, track in enumerate(duplicates, start=1):
            # Format playlist 1 albums
            playlist_one_albums_str = ", ".join(
                [album['album'] for album in track['playlist_one_albums']]
            )

            # Format playlist 2 albums (if populated)
            if track['playlist_two_albums']:
                playlist_two_albums_str = ", ".join(
                    [album['album'] for album in track['playlist_two_albums']]
                )
                # Write with both playlists
                f.write(f"{i}. {track['artist']} - {track['title']} "
                        f"\n\tPlaylist 1: {playlist_one_albums_str}"
                        f"\n\tPlaylist 2: {playlist_two_albums_str}\n\n")
            else:
                # Write with only playlist 1 on a single line
                f.write(f"{i}. {track['artist']} - {track['title']} "
                        f"({playlist_one_albums_str})\n")
