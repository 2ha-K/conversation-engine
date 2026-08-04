from abc import ABC, abstractmethod
from pathlib import Path


class Player(ABC):
    """Abstract base class for audio playback."""

    @abstractmethod
    def play(self, path: Path) -> None:
        """Play an audio file."""
        pass