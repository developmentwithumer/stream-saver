from yt_dlp import YoutubeDL
from format import format_duration, format_filesize, format_views

def Downloader(url):
    """
    Fetches video details using yt-dlp, returning only valid download URLs for different resolutions, excluding .m3u8 URLs.

    Args:
        url (str): URL of the video to fetch information for.

    Returns:
        dict: A dictionary containing video details like title, description, views, duration,
              and valid download URLs for multiple resolutions (excluding .m3u8 links).
    """
    options = {
        'quiet': True,  # Suppress unnecessary logs
        'noplaylist': True,  # Ensure we're processing a single video
    }

    with YoutubeDL(options) as ydl:
        try:
            # Extract video information
            info = ydl.extract_info(url, download=False)

            # Parse relevant details
            video_details = {
                'title': info.get('title'),
                'thumbnail': info.get('thumbnail'),
                'description': info.get('description'),
                'views': format_views(info.get('view_count')),
                'duration': format_duration(info.get('duration')),  # Duration in seconds
                'valid_formats': []  # List to hold valid download URLs for different resolutions
            }

            # Extract available formats (resolutions)
            for format in info.get('formats', []):
                download_url = format.get('url')
                # Exclude .m3u8 URLs and ensure it's a valid video format with URL, video codec, and audio codec
                if download_url and format.get('vcodec') != 'none' and format.get('acodec') != 'none' and not download_url.endswith('.m3u8'):
                    video_details['valid_formats'].append({
                        'resolution': format.get('format_note'),
                        'download_url': download_url,
                        'ext': format.get('ext'),
                        'filesize': format_filesize(format.get('filesize'))
                    })

            # Remove duplicate resolutions
            unique_resolutions = {}
            for format in video_details['valid_formats']:
                resolution = format['resolution']
                if resolution not in unique_resolutions:
                    unique_resolutions[resolution] = format

            # Update valid_formats with unique resolutions
            video_details['valid_formats'] = list(unique_resolutions.values())

            return video_details

        except Exception as e:
            print(f"Error: {e}")
            return None