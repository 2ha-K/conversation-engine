from agent.brains.base import BaseBrain

class FastBrain(BaseBrain):
    """Handles quick responses without using memory or external tools."""
    def __init__(self, model):
        self.model = model
    def respond(self, text: str) -> str:
        return self.model.generate(text)

