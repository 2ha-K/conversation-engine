from abc import ABC, abstractmethod

class BrainSelector(ABC):

    @abstractmethod
    def select(self, text: str):
        pass