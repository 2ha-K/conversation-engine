from audio.data import AudioData
class ConversationOrchestrator:
    """Orchestrates the conversation flow between ASR, Memory, LLM, and TTS components."""
    def __init__(self, asr, agent, tts):
        self.asr = asr
        self.agent = agent
        self.tts = tts

    def handle_conversation(self, audio: AudioData)-> None:
        text = self.asr.transcrible(audio)

        response = self.agent.respond(text)

        self.tts.speak(response)

    def handle_interrupt(self):
        pass


class ASR:
    """Handles Automatic Speech Recognition (ASR) to convert spoken language into text."""
    def __init__(self, recognizer):
        self.recognizer = recognizer

    def transcrible(self, audio)-> str:
        text = self.recognizer.transcribe(audio)
        return text


class Agent:
    """Represents an agent that can respond to text input using a selected brain."""
    def __init__(self, selector):
        self.selector = selector

    def respond(self, text):
        brain = self.selector.select(text)
        return brain.respond(text)


class TTS:
    """Handles Text-to-Speech (TTS) to convert text into spoken language."""
    def speak(self, text: str)-> None:
        print(f"Speaking: {text}")