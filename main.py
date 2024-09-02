#!/usr/bin/env python3

import os
import sys
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import click

# Load environment variables from .env file
load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI = os.getenv('SPOTIPY_REDIRECT_URI')

scope = 'playlist-modify-public playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                               client_secret=SPOTIPY_CLIENT_SECRET,
                                               redirect_uri=SPOTIPY_REDIRECT_URI,
                                               scope=scope))

@click.command()
@click.argument('playlist1_url')
@click.argument('playlist2_url', required=False)  # Second playlist URL is now optional
@click.option('--output', type=click.Path(), help='Path to the output file')
@click.option('--delete-duplicates', is_flag=True, help='Delete duplicates from second playlist')
def find_duplicates(playlist1_url, playlist2_url=None, output=None, delete_duplicates=False):
  playlist1_tracks = get_playlist_tracks(playlist1_url)

  if playlist2_url:
    playlist2_tracks = get_playlist_tracks(playlist2_url)
    if output:
      find_and_print_duplicates(playlist1_tracks, playlist2_tracks, output)
    else:
      find_and_print_duplicates(playlist1_tracks, playlist2_tracks)
    
    if delete_duplicates:
      duplicates = get_duplicate_tracks()
      # remove_duplicate_tracks(playlist2_url, duplicates)
      click.echo(f"Removed {len(duplicates)} duplicates from the second playlist.")
  else:
    if output:
      find_and_print_duplicates_within_playlist(playlist1_tracks, output)
    else:
      find_and_print_duplicates_within_playlist(playlist1_tracks)

def get_playlist_tracks(playlist_url):
  playlist_id = extract_playlist_id(playlist_url)
  results = sp.playlist_tracks(playlist_id)
  tracks = results['items']

  while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

  return [track['track'] for track in tracks]

def extract_playlist_id(playlist_url):
  return playlist_url.split('/')[-1].split('?')[0]

def find_and_print_duplicates(playlist1_tracks, playlist2_tracks, output_file=None):
  # Create a dictionary with preview_url as keys and details as values for playlist 1
  playlist1_details = {}
  for track in playlist1_tracks:
    if track['preview_url']:
      playlist1_details[track['preview_url']] = {
        'artist': track['artists'][0]['name'],
        'title': track['name'],
        'album': track['album']['name'],
        'type': track['album']['album_type']
      }

  duplicates = []
  for track in playlist2_tracks:
    preview_url = track['preview_url']
    if preview_url in playlist1_details:
      duplicates.append({
        'artist': track['artists'][0]['name'],
        'title': track['name'],
        'album1': playlist1_details[preview_url]['album'],
        'type1': playlist1_details[preview_url]['type'],
        'album2': track['album']['name'],
        'type2': track['album']['album_type']
      })

  # Print total tracks found in green
  total_tracks = len(duplicates)
  print(f"\033[92mTotal Tracks Found: {total_tracks}\033[0m")

  # Print each duplicate with colored album names and number each track
  for i, track in enumerate(duplicates, start=1):
    album1_colored = colorize_album(track['album1'], track['type1'])
    album2_colored = colorize_album(track['album2'], track['type2'])
    print(f"{i}. {track['artist']} - {track['title']} ({album1_colored} & {album2_colored})")

  # Write to output file if provided
  if output_file:
    with open(output_file, 'w') as f:
      for i, track in enumerate(duplicates, start=1):
        f.write(f"{i}. {track['artist']} - {track['title']} ({track['album1']} & {track['album2']})\n")

    # Print the content of the output file in green
    print_in_terminal(output_file)

def find_and_print_duplicates_within_playlist(playlist_tracks, output_file=None):
  preview_urls = {}
  duplicates = []

  for track in playlist_tracks:
    if track['preview_url']:
      preview_url = track['preview_url']
      if preview_url in preview_urls:
        duplicates.append({
          'artist': track['artists'][0]['name'],
          'title': track['name'],
          'album': track['album']['name'],
          'type': track['album']['album_type']
        })
      else:
        preview_urls[preview_url] = {
          'artist': track['artists'][0]['name'],
          'title': track['name'],
          'album': track['album']['name'],
          'type': track['album']['album_type']
        }

  # Print total tracks found in green
  total_tracks = len(duplicates)
  print(f"\033[92mTotal Tracks Found: {total_tracks}\033[0m")

  # Print each duplicate with colored album names and number each track
  for i, track in enumerate(duplicates, start=1):
    album_colored = colorize_album(track['album'], track['type'])
    print(f"{i}. {track['artist']} - {track['title']} ({album_colored})")

  # Write to output file if provided
  if output_file:
    with open(output_file, 'w') as f:
      for i, track in enumerate(duplicates, start=1):
        f.write(f"{i}. {track['artist']} - {track['title']} ({track['album']})\n")

    # Print the content of the output file in green
    print_in_terminal(output_file)

def remove_duplicate_tracks(playlist_url, duplicates):
  playlist_id = extract_playlist_id(playlist_url)
  track_uris = [track['uri'] for track in duplicates]
  sp.playlist_remove_all_occurrences_of_items(playlist_id, track_uris)

def colorize_album(album_name, album_type):
  colors = {
    'album': '\033[94m',  # Blue
    'single': '\033[91m', # Red
    'compilation': '\033[93m',  # Yellow for compilation EPs
    'ep': '\033[93m'  # Yellow
  }
  color = colors.get(album_type, '\033[0m')  # Default to no color
  return f"{color}{album_name}\033[0m"

def print_in_terminal(file_path):
  # Print the content of the output file in green
  with open(file_path, 'r') as f:
    content = f.read()
    print(f"\033[92m{content}\033[0m")

if __name__ == '__main__':
  find_duplicates()