import os
from typing import List

# Supported audio file extensions
SUPPORTED_EXTENSIONS = {'.mp3', '.wav', '.flac', '.mp4', '.aac', '.ogg', '.wma', '.m4a'}

def is_supported_file(filename: str) -> bool:
    _, ext = os.path.splitext(filename)
    return ext.lower() in SUPPORTED_EXTENSIONS


def scan_music_files(base_path: str) -> List[str]:
    """Recursively scans base_path for audio files and returns a list of full file paths."""
    audio_files = []
    for root, _, files in os.walk(base_path):
        for file in files:
            if is_supported_file(file):
                audio_files.append(os.path.join(root, file))
    return audio_files

# Example usage (for tests):
# music_files = scan_music_files("/media/usb0")
# print(music_files)
