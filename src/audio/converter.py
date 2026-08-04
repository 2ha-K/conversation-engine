from abc import ABC, abstractmethod
from pathlib import Path


class AudioConverter(ABC):

    @abstractmethod
    def to_wav(self, input_path: Path, output_path: Path) -> Path:
        """Convert an audio file to WAV."""
        pass