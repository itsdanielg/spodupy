def get_duplicates(playlist1_tracks, playlist2_tracks=None):
    playlist_details = {}

    def process_tracks(tracks, playlist_key):
        if tracks is None:
            return

        for track in tracks:
            preview_url = track.get('preview_url')
            if not preview_url:
                continue

            # Initialize the track details if it's not already in the playlist_details
            if preview_url not in playlist_details:
                playlist_details[preview_url] = {
                    'artist': track['artists'][0]['name'],
                    'title': track['name'],
                    'playlist_one_albums': [],
                    'playlist_two_albums': []
                }

            # Append the current track's album, type, and ID to the correct playlist's arrays
            playlist_details[preview_url][playlist_key].append({
                'album': track['album']['name'],
                'type': track['album']['album_type'],
                'id': track['id']  # Add track ID here
            })

    # Process playlist 1 tracks
    process_tracks(playlist1_tracks, 'playlist_one_albums')

    # Process playlist 2 tracks if provided
    process_tracks(playlist2_tracks, 'playlist_two_albums')

    # Find duplicates based on album presence in both playlists
    duplicates = []
    for preview_url, details in playlist_details.items():
        if len(details['playlist_one_albums']) > 1 or (len(details['playlist_one_albums']) > 0 and len(details['playlist_two_albums']) > 0):
            # If there are albums in both playlists, it's considered a duplicate
            duplicates.append({
                'artist': details['artist'],
                'title': details['title'],
                'playlist_one_albums': details['playlist_one_albums'],
                'playlist_two_albums': details['playlist_two_albums']
            })

    return duplicates
