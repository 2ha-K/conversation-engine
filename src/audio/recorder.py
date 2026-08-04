from pathlib import Path
from audio.data import AudioData

class Recorder:

    def record(self) -> AudioData:
        return AudioData(path=Path("data/audio/input/temp.mp3"))