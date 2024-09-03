from spdu.utils import get_colored_album_str, get_colored_str


def print_duplicates(duplicates):
    print(get_colored_str(f"\nTotal Tracks Found: {
          len(duplicates)}", "green") + "\n")

    for i, track in enumerate(duplicates, start=1):
        # Format playlist 1 albums
        playlist_one_albums_str = ", ".join(
            [get_colored_album_str(album['album'], album['type'])
             for album in track['playlist_one_albums']]
        )

        # Format playlist 2 albums (if populated)
        if track['playlist_two_albums']:
            playlist_two_albums_str = ", ".join(
                [get_colored_album_str(album['album'], album['type'])
                 for album in track['playlist_two_albums']]
            )
            # Print with both playlists
            print(f"{i}. {track['artist']} - {track['title']} "
                  f"\n\tPlaylist 1: {playlist_one_albums_str}"
                  f"\n\tPlaylist 2: {playlist_two_albums_str}\n")
        else:
            # Print with only playlist 1 on a single line
            print(f"{i}. {track['artist']} - {track['title']
                                              } ({playlist_one_albums_str})")


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
