# Youtube video downloader and converter
Download videos from YouTube, convert them to .WAV and crop them to short segments


# Usage:
* Run as following:
python3 down_crop.py <youtube-link> <start_time in mm:ss format> <length in seconds ss formart> <y/n - remove_originals> <y/n download_from_playlist>

# Dependecies:
- brew install youtube-dl
- brew install ffmpeg

* python packages:
- sys
- subprocess
- uuid
