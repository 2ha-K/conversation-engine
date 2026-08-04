class Agent:
    """Represents an agent that can respond to text input using a selected brain."""
    def __init__(self, selector):
        self.selector = selector

    def respond(self, text):
        brain = self.selector.select(text)
        return brain.respond(text)