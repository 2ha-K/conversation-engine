from abc import ABC, abstractmethod

class BaseBrain(ABC):

    @abstractmethod
    def respond(self, text: str) -> str:
        """Generate a response."""
        pass