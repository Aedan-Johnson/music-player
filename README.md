# USB Music Player

A GUI program made with Python to provide a modern graphical interface for your music library on a USB drive or folder. Supports MP3, WAV, FLAC, MP4, and many more formats, with playback controls, queue/shuffle, and now playing info.

---

## Features
- **Automatic Music Discovery:** Recursively finds all music on your USB drive or chosen folder
- **Supported Formats:** MP3, WAV, FLAC, MP4, OGG, AAC, M4A, WMA
- **Modern GUI:** Easy-to-use interface built with PyQt6
- **Playback Controls:** Play, pause, next, previous, shuffle, and queue navigation
- **Now Playing:** Always know what’s currently playing
- **Shuffle Mode:** Play music in random order
- **No Internet Required:** 100% offline desktop app

---

## Getting Started
1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Plug in your USB drive** (or prepare a music folder)

3. **Run the app:**
   ```bash
   python src/main.py
   ```

4. **Select your music folder** when prompted, or use the default USB scan.

---

## Usage
- Double-click a song to play it
- Use Play, Pause, Next, Previous for playback control
- Hit Shuffle to randomize the queue
- Click "Load Folder" to scan a different music source (like another USB drive)

---

## Troubleshooting
- If no music appears, make sure your USB is mounted and contains supported files
- The app will pick the first available folder with music under `/media` by default; you can select another folder with "Load Folder"
- You may need VLC installed on your system for `python-vlc` playback (see [python-vlc docs](https://pypi.org/project/python-vlc/))

---

## How it Works
- Uses recursive file search for supported formats
- Audio playback via python-vlc for broad codec compatibility
- All controls run locally in a modern PyQt6 interface

---

## Project Structure
```
/src
  /gui
    main_window.py      # Main application window (GUI)
    playlist_widget.py  # Playlist display logic
    player_controls.py  # Controls panel code
  /player
    audio_engine.py     # Handles audio playback and queue
    queue_manager.py    # Queue and shuffle logic
    metadata_reader.py  # Reads metadata from files
  /storage
    usb_scanner.py      # USB and folder scanning routines
  /utils
    constants.py        # Format/extensions, etc.
main.py                # App entrypoint
```

---

## Contributing
Pull requests are welcome! For suggestions, please open an issue first.

---

## License
[MIT](LICENSE)
