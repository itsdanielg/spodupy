import click
from spotify_client import get_playlist_tracks, find_and_print_duplicates, find_and_print_duplicates_within_playlist, remove_duplicate_tracks


@click.command()
@click.argument('playlist1_url')
# Second playlist URL is now optional
@click.argument('playlist2_url', required=False)
@click.option('--output', type=click.Path(), help='Path to the output file')
@click.option('--delete-duplicates', is_flag=True, help='Delete duplicates from second playlist')
def find_duplicates(playlist1_url, playlist2_url=None, output=None, delete_duplicates=False):
    playlist1_tracks = get_playlist_tracks(playlist1_url)

    if playlist2_url:
        playlist2_tracks = get_playlist_tracks(playlist2_url)
        duplicates = find_and_print_duplicates(
            playlist1_tracks, playlist2_tracks, output)

        if delete_duplicates and duplicates:
            remove_duplicate_tracks(playlist2_url, duplicates)
            click.echo(f"Removed {len(duplicates)
                                  } duplicates from the second playlist.")
    else:
        find_and_print_duplicates_within_playlist(playlist1_tracks, output)
