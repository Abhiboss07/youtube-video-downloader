import os
import sys
from yt_dlp import YoutubeDL

def download_video(video_url):
    options = {
        'outtmpl': '%(title)s.%(ext)s',
        'format': 'best',
    }

    with YoutubeDL(options) as ydl:
        ydl.download([video_url])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python download.py <video_url>")
        sys.exit(1)

    video_url = sys.argv[1]
    download_video(video_url)
