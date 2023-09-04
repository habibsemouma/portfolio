import yt_dlp
import time
import os
def videotomp3(url):
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        "outtmpl":"ytbmp3/videos/%(title)s.%(ext)s",
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        video_title = info_dict.get('title', 'video')
        filename = ydl.prepare_filename(info_dict)
        ydl.download(url)
    return filename,video_title

def delete_file(file_path, delay):
    time.sleep(delay)
    try:
        os.remove(file_path)
    except Exception as e:
        print(f"Error deleting file: {e}")


