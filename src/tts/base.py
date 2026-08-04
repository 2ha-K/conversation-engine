from abc import ABC, abstractmethod

class TTS(ABC):
    """Handles Text-to-Speech (TTS) to convert text into spoken language."""
    @abstractmethod
    def speak(self, text: str) -> None:
        pass