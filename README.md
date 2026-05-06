# USB Music Player

A GUI program made with Python to provide a modern graphical interface for your music library on a USB drive or folder. Supports MP3, WAV, FLAC, MP4, and more, with playback controls, queue/shuffle, and now playing info.

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

## 🚀 Installation (Quick Start)

Follow these steps to quickly get the app up and running:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aedan-Johnson/music-player.git
   cd music-player
   ```

2. **(Recommended) Create a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Python Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install VLC Media Player (Required for Audio Playback)**
   - **Windows/macOS:** [Download VLC](https://www.videolan.org/vlc/) and install it normally.
   - **Linux (Ubuntu):**
     ```bash
     sudo apt install vlc
     ```
   - VLC must be available on your system PATH so `python-vlc` can use it!

5. **Plug in your USB drive** (or prepare a folder with music files).

6. **Run the App**
   ```bash
   python src/main.py
   ```

7. **Select your music folder** when prompted (or the app will try to auto-detect).


---

## Usage
- Double-click a song in the list to play it
- Use Play, Pause, Next, Previous for playback control
- Hit Shuffle to randomize the queue
- Click "Load Folder" to scan a different music source (like another USB drive)

---

## Troubleshooting
- **No music appears:** Ensure your USB is mounted and contains music in supported formats.
- **No sound:** Make sure VLC Player is installed and working on your system.
- **App won’t start:** Ensure you are in the correct Python environment and dependencies are installed.
- For advanced VLC errors, see [python-vlc documentation](https://pypi.org/project/python-vlc/) or [VLC support](https://www.videolan.org/support/).

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
