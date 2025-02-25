# Spodupy

Spodupy is a Python CLI tool that identifies duplicate tracks within and between Spotify playlists. Duplicates are determined based on the ISRC (International Standard Recording Code) of tracks, so even identical songs from different albums are properly recognized.

## Features

- Detect duplicate tracks between one or two playlists
- Detect duplicates on public and private playlists (to be added)
- Ability to remove duplicate tracks (to be added)

## Prerequisites

Make sure the following are installed before proceeding:

- Python 3.12.5+ (Check with `python --version`)
- pip (Check with `pip --version`)
- git (Check with `git --version`)

## Installation and Setup

Clone this repository and install with pip.

```bash
git clone https://github.com/itsdanielg/spodupy
cd spodupy
pip install .
```

## Setup

This tool requires an app to be created on your **Spotify Developer Dashboard**, as it requires API calls.

### Steps:

1. Navigate to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Click **Create app**, then fill out all required fields
3. In the **Redirect URIs** section, enter the same URI found in your `.env` file
4. Ensure **Web API** is checked
5. Click **Save** to finalize the app
6. After creation, navigate to **Settings** in the dashboard.
7. Copy your **Client ID** and paste it into the `.env` file:

```bash
SPODUPY_CLIENT_ID=your_client_id
```

8. Copy your **Client Secret** and paste it into the `.env` file:

```bash
SPODUPY_CLIENT_SECRET=your_client_secret
```

9. Save the `.env` file

## Usage

Once installed, you can use the `spdu` command to run the program.

```bash
spdu [options] [urls]
```

### Options

- `--output <file>`: (Optional) Specify an output file where the duplicates will be listed.
- `--reset-cache`: (Optional) Reset the cache and fetch fresh data from Spotify.

### Examples

**Find duplicates in a single playlist:**

```bash
spdu https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=2ebb19b1c6f8494a

--------------------------------
Duplicates by ID
Total Tracks Found: 0
--------------------------------
Duplicates by Track
Total Tracks Found: 1

1.	Porter Robinson - Russian Roulette (SMILE! :D) [playlist1]
2.	Porter Robinson - Russian Roulette (Russian Roulette) [playlist1]

```

**Find duplicates between two playlists:**

```bash
spdu https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=2ebb19b1c6f8494a https://open.spotify.com/playlist/37i9dQZF1DX0XUsuxWHRQd?si=20cb117afe5e47cc

--------------------------------
Duplicates by ID
Total Tracks Found: 1

1.	Porter Robinson - Russian Roulette (SMILE! :D) [playlist1]
1.	Porter Robinson - Russian Roulette (SMILE! :D) [playlist2]
--------------------------------
Duplicates by Track
Total Tracks Found: 1

1.	Porter Robinson - Russian Roulette (SMILE! :D) [playlist1]
2.	Porter Robinson - Russian Roulette (Russian Roulette) [playlist2]
--------------------------------

```

**Find duplicates and save results to a file:**

```bash
spdu --output duplicates.txt https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M?si=2ebb19b1c6f8494a
```

## How It Works

- **ISRC Matching**: `spdu` uses the ISRC (International Standard Recording Code) of tracks to determine duplicates. Even if two identical tracks are in different albums or playlists, they will be flagged as duplicates if their ISRCs match.
- **Cache**: Playlist data is cached to avoid unnecessary API calls and to speed up subsequent checks. Use the `--reset-cache` option if you want to fetch fresh data from Spotify.
