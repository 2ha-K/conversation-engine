from abc import ABC, abstractmethod

from audio.data import AudioData


class ASR(ABC):

    @abstractmethod
    def transcribe(self, audio: AudioData) -> str:
        ...