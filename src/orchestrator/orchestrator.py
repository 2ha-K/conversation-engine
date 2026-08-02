class ConversationOrchestrator:
    """Orchestrates the conversation flow between ASR, Memory, LLM, and TTS components."""
    def __init__(self, asr, memory, llm, tts):
        self.asr = asr
        self.memory = memory
        self.llm = llm
        self.tts = tts

    def handle_conversation(self)-> None:
        text = self.asr.listen()

        context = self.memory.search(text)

        response = self.llm.generate(text, context)

        self.tts.speak(response)

    def handle_interrupt(self):
        pass


class ASR:
    """Handles Automatic Speech Recognition (ASR) to convert spoken language into text."""
    def listen(self)-> str:
        print("Listening...")
        return "你好"


class Memory:
    """Manages the storage from memory. (Can be a database, file system, or any other storage mechanism.)"""
    def search(self, query: str)-> list:
        print(f"Searching memory: {query}")
        return []

    def save(self, memory: str)-> None:
        print(f"Saving to memory: {memory}")


class LLM:
    """Handles the Language Model to generate responses based on input text and context."""
    def generate(self, text: str, context: list)-> str:
        print("Generating response...")
        return "你好，很高興見到你！"


class TTS:
    """Handles Text-to-Speech (TTS) to convert text into spoken language."""
    def speak(self, text: str)-> None:
        print(f"Speaking: {text}")