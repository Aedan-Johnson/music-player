import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton,
    QLabel, QListWidget, QFileDialog, QMessageBox
)
from PyQt6.QtCore import Qt
import os

from storage.usb_scanner import scan_music_files
from player.audio_engine import AudioEngine

MUSIC_PATH_GUESS = "/media"  # set to drive mount on your OS

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("USB Music Player")
        self.resize(900, 650)
        self.music_files = []
        self.audio_engine = AudioEngine(on_end=self.handle_track_end)

        self.central = QWidget()
        self.setCentralWidget(self.central)
        self.layout = QVBoxLayout()
        self.central.setLayout(self.layout)

        # Now playing label
        self.now_playing = QLabel("Now Playing: None")
        self.layout.addWidget(self.now_playing)

        # Song list
        self.songs_list = QListWidget()
        self.songs_list.itemDoubleClicked.connect(self.play_selected_song)
        self.layout.addWidget(self.songs_list)

        # Controls
        controls = QHBoxLayout()
        self.btn_prev = QPushButton("Previous")
        self.btn_play = QPushButton("Play")
        self.btn_pause = QPushButton("Pause")
        self.btn_next = QPushButton("Next")
        self.btn_shuffle = QPushButton("Shuffle")
        self.btn_load = QPushButton("Load Folder")
        controls.addWidget(self.btn_prev)
        controls.addWidget(self.btn_play)
        controls.addWidget(self.btn_pause)
        controls.addWidget(self.btn_next)
        controls.addWidget(self.btn_shuffle)
        controls.addWidget(self.btn_load)
        self.layout.addLayout(controls)

        self.btn_prev.clicked.connect(self.play_prev)
        self.btn_play.clicked.connect(self.play_current)
        self.btn_pause.clicked.connect(self.audio_engine.pause)
        self.btn_next.clicked.connect(self.play_next)
        self.btn_shuffle.clicked.connect(self.shuffle_and_play)
        self.btn_load.clicked.connect(self.choose_and_load_folder)

        # Load music on start
        self.load_music_folder(self.detect_default_music_folder())

    def detect_default_music_folder(self):
        candidate = MUSIC_PATH_GUESS
        if os.path.exists(candidate):
            # Pick first USB subfolder with files
            for entry in os.scandir(candidate):
                if entry.is_dir() and len(os.listdir(entry.path)) > 0:
                    return entry.path
        return os.path.expanduser("~")  # fallback to home

    def load_music_folder(self, folder):
        self.music_files = scan_music_files(folder)
        if not self.music_files:
            QMessageBox.warning(self, "No Music Found", "No supported music files found in this folder.")
        self.songs_list.clear()
        # Show file names for now
        for f in self.music_files:
            self.songs_list.addItem(os.path.basename(f))
        self.audio_engine.set_playlist(self.music_files)
        if self.music_files:
            self.now_playing.setText("Now Playing: " + os.path.basename(self.music_files[0]))
        else:
            self.now_playing.setText("Now Playing: None")

    def choose_and_load_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Music Folder")
        if folder:
            self.load_music_folder(folder)

    def play_selected_song(self, item):
        idx = self.songs_list.row(item)
        self.audio_engine.play_index(idx)
        self.now_playing.setText("Now Playing: " + item.text())

    def play_current(self):
        idx = self.songs_list.currentRow()
        if idx >= 0:
            self.audio_engine.play_index(idx)
            self.now_playing.setText("Now Playing: " + self.songs_list.currentItem().text())

    def play_next(self):
        self.audio_engine.next()
        idx = self.audio_engine.current_index
        if self.music_files and idx < len(self.music_files):
            self.now_playing.setText("Now Playing: " + os.path.basename(self.music_files[idx]))
            self.songs_list.setCurrentRow(idx)

    def play_prev(self):
        self.audio_engine.previous()
        idx = self.audio_engine.current_index
        if self.music_files and idx < len(self.music_files):
            self.now_playing.setText("Now Playing: " + os.path.basename(self.music_files[idx]))
            self.songs_list.setCurrentRow(idx)

    def shuffle_and_play(self):
        import random
        random.shuffle(self.music_files)
        self.songs_list.clear()
        for f in self.music_files:
            self.songs_list.addItem(os.path.basename(f))
        self.audio_engine.set_playlist(self.music_files)
        self.audio_engine.play_index(0)
        if self.music_files:
            self.now_playing.setText("Now Playing: " + os.path.basename(self.music_files[0]))
            self.songs_list.setCurrentRow(0)

    def handle_track_end(self):
        self.play_next()

def run_app():
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
