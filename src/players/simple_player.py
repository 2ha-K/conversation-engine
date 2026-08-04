from pathlib import Path

import pygame

from players.base import Player


class SimplePlayer(Player):
    """Play audio through the system speaker."""

    def __init__(self):
        pygame.mixer.init()

    def play(self, path: Path=Path("data/audio/output/tts.wav")) -> None:
        pygame.mixer.music.load(str(path))
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    