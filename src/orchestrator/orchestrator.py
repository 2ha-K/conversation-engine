class ConversationOrchestrator:

    def __init__(self, asr, memory, llm, tts):
        self.asr = asr
        self.memory = memory
        self.llm = llm
        self.tts = tts

    def handle_conversation(self):
        pass

    def handle_interrupt(self):
        pass


class ASR:
    def listen(self):
        pass


class Memory:
    def search(self, query):
        pass

    def save(self, memory):
        pass


class LLM:
    def generate(self, text, context):
        pass


class TTS:
    def speak(self, text):
        pass