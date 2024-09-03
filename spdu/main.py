import click

from spdu.get_duplicates import get_duplicates
from spdu.api import fetch_playlist_tracks, delete_playlist_tracks
from spdu.print import print_duplicates, print_duplicates_to_output


@click.command()
@click.argument('playlist1_url')
# Second playlist URL is now optional
@click.argument('playlist2_url', required=False)
@click.option('--output', type=click.Path(), default=None, help='Path to the output file. If not provided, no output will be set.')
@click.option('--delete-duplicates', is_flag=True, help='Delete duplicates from second playlist')
def main(playlist1_url, playlist2_url=None, output=None, delete_duplicates=False):
    playlist1_tracks = fetch_playlist_tracks(playlist1_url)
    playlist2_tracks = fetch_playlist_tracks(playlist2_url)

    duplicates = get_duplicates(playlist1_tracks, playlist2_tracks)
    print_duplicates(duplicates)

    if output is not None:
        print_duplicates_to_output(duplicates, output)

    if delete_duplicates and playlist2_url and duplicates:
        delete_playlist_tracks(playlist2_url, duplicates)
