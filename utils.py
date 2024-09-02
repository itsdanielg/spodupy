def colorize_album(album_name, album_type):
    colors = {
        'album': '\033[94m',  # Blue
        'single': '\033[91m',  # Red
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
