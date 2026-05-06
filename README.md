# USB Music Player

A GUI program made with Python that provides a visual music library/player for songs on a USB drive (`.mp3`, `.mp4`, etc). Features shuffle, queue display, metadata, and more.

## Features (Planned)
- Detect and load music from USB drives
- Shuffle, queue management, next/previous track
- Album/track metadata display (artist, title, duration)
- Clean, modern GUI (with PyQt6)
- Playback powered by `python-vlc`

## Getting Started

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app:**
   ```bash
   python src/main.py
   ```

## Roadmap
- [x] Project scaffold
- [ ] Implement USB drive scanner
- [ ] Build out GUI components
- [ ] Add playback and queue logic
