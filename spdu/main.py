import click

from spdu.cache import get_playlist
from spdu.get_duplicates import get_all_duplicate_or_unique_tracks
from spdu.models import ApiPlaylist
from spdu.print import print_duplicates


@click.command()
@click.argument('playlist_one_url')
@click.argument('playlist_two_url', required=False)
@click.option('--output', type=click.Path(), default=None, help='Path to the output file. If omitted, no output file will be created.')
@click.option('--reset-cache', is_flag=True, help='Resets playlist cache and rewrites JSON file')
@click.option('--get-unique', is_flag=True, help='Get all unique tracks in a playlist instead of duplicates')
def main(playlist_one_url, playlist_two_url=None, output=None, reset_cache=True, get_unique=False):

    playlist_one: ApiPlaylist = get_playlist(playlist_one_url, reset_cache)
    playlist_two: ApiPlaylist = get_playlist(playlist_two_url, reset_cache)

    duplicates = get_all_duplicate_or_unique_tracks(
        playlist_one, playlist_two, get_unique)
    print("\n--------------------------------")
    print("Duplicates by ID")
    print_duplicates(duplicates[0])
    print("--------------------------------")
    print("Duplicates by Track")
    print_duplicates(duplicates[1])
    print("--------------------------------\n")

    # if output is not None:
    #     print_duplicates_to_output(duplicates, output)
