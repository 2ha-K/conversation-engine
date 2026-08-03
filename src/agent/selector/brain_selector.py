class BrainSelector:

    def __init__(self, fast_brain, medium_brain, slow_brain):
        self.fast_brain = fast_brain
        self.medium_brain = medium_brain
        self.slow_brain = slow_brain

    def select(self, text: str):
        return self.fast_brain