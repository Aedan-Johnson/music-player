import vlc
from typing import Callable, List, Optional

class AudioEngine:
    def __init__(self, on_end: Optional[Callable]=None):
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()
        self.media_list: List[str] = []
        self.current_index: int = 0
        self.on_end = on_end
        self.is_playing = False
        self._setup_events()

    def _setup_events(self):
        events = self.player.event_manager()
        events.event_attach(vlc.EventType.MediaPlayerEndReached, self._handle_end)

    def _handle_end(self, event):
        if self.on_end:
            self.on_end()

    def set_playlist(self, media_list: List[str]):
        self.media_list = media_list
        self.current_index = 0

    def play_index(self, idx: int):
        if 0 <= idx < len(self.media_list):
            self.current_index = idx
            self.stop()
            media = self.instance.media_new(self.media_list[idx])
            self.player.set_media(media)
            self.player.play()
            self.is_playing = True

    def play(self):
        if not self.is_playing:
            self.player.play()
            self.is_playing = True

    def pause(self):
        if self.player:
            self.player.pause()
            self.is_playing = False

    def stop(self):
        if self.player:
            self.player.stop()
            self.is_playing = False

    def next(self):
        if self.current_index + 1 < len(self.media_list):
            self.play_index(self.current_index + 1)

    def previous(self):
        if self.current_index - 1 >= 0:
            self.play_index(self.current_index - 1)

    def get_current_file(self) -> Optional[str]:
        if self.media_list and 0 <= self.current_index < len(self.media_list):
            return self.media_list[self.current_index]
        return None
