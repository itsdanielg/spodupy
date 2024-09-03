def extract_playlist_id(playlist_url):
    return playlist_url.split("/")[-1].split("?")[0]


def get_colored_str(text, color):
    # Define color codes
    colors = {
        'green': '\033[92m',  # Green
        'red': '\033[91m',    # Red
        'yellow': '\033[93m'  # Yellow
    }

    # Get the color code, default to no color if the color is not recognized
    color_code = colors.get(color.lower(), '\033[0m')

    # Return the colored text
    return f"{color_code}{text}\033[0m"


def get_colored_album_str(album_name, album_type):
    colors = {
        'album': '\033[94m',  # Blue
        'single': '\033[91m',  # Red
        'compilation': '\033[93m',  # Yellow for compilation EPs
    }
    color = colors.get(album_type, '\033[0m')  # Default to no color
    return f"{color}{album_name}\033[0m"


def print_in_terminal(file_path):
    # Print the content of the output file in green
    with open(file_path, 'r') as f:
        content = f.read()
        print(f"\033[92m{content}\033[0m")
