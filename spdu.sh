#!/bin/bash

# Path to your virtual environment
VENV_PATH="$HOME/Development/spotify-duplicates/"

# Path to your Python script
SCRIPT_PATH="$HOME/Development/spotify-duplicates/main.py"

# Define an absolute path for cache
CACHE_PATH="$HOME/.cache/spotipy_cache"

# Activate the virtual environment
source "$VENV_PATH/myenv/bin/activate"

# Run the Python script
python3 "$SCRIPT_PATH" "$@"

# Deactivate the virtual environment
deactivate