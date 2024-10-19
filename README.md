# Spotoolfy

Spotoolfy is a command-line tool designed to help you identify duplicate tracks in and between Spotify playlists. Duplicates are determined based on the ISRC (International Standard Recording Code) of tracks, ensuring that identical songs from different albums are properly recognized.

## Features

- Detect duplicates between one or two playlists.
- Duplicates are identified using the ISRC of each track.

## Installation

You can install `spotoolfy` using `pip`:

```bash
pip install spdu
```

## Usage

Once installed, you can use the `spdu` command to detect duplicates in Spotify playlists.

### Basic Syntax

```bash
spdu [options] [urls]
```

### Options

- `--output <file>`: (Optional) Specify an output file where the duplicates will be listed.
- `--delete`: (Optional) Remove duplicates from the second playlist, if two playlists are provided.
- `--reset-cache`: (Optional) Reset the cache and fetch fresh data from Spotify.

### Examples

1. **Find duplicates in a single playlist:**

```bash
spdu https://open.spotify.com/playlist/1hZkQLaEos7PzM2FnYaA0X
```

2. **Find duplicates between two playlists:**

```bash
spdu https://open.spotify.com/playlist/1hZkQLaEos7PzM2FnYaA1K https://open.spotify.com/playlist/2gZkQLjUos7QfF8FnYaA1K
```

3. **Find duplicates and save results to a file:**

```bash
spdu --output duplicates.txt https://open.spotify.com/playlist/1hZkQLaEos7PzM2FnYaA0X
```

4. **Remove duplicates from the second playlist:**

```bash
spdu --delete https://open.spotify.com/playlist/1hZkQLaEos7PzM2FnYaA0X https://open.spotify.com/playlist/2gZkQLjUos7QfF8FnYaA1K
```

## How It Works

- **ISRC Matching**: `spdu` uses the ISRC (International Standard Recording Code) of tracks to determine duplicates. Even if two identical tracks are in different albums or playlists, they will be flagged as duplicates if their ISRCs match.
- **Cache**: Playlist data is cached to avoid unnecessary API calls and to speed up subsequent checks. Use the `--reset-cache` option if you want to fetch fresh data from Spotify.
