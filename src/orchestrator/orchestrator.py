from audio.data import AudioData
from tts.base import TTS
from agent.base import Agent
from asr.base import ASR
from players.base import Player
class ConversationOrchestrator:
    """Orchestrates the conversation flow between ASR, Memory, LLM, and TTS components."""
    def __init__(self, asr: ASR, agent: Agent, tts: TTS, player: Player):
        self.asr = asr
        self.agent = agent
        self.tts = tts
        self.player = player

    def handle_conversation(self, audio: AudioData)-> None:
        print("=== Conversation Start ===")

        text = self.asr.transcribe(audio)
        print(f"[ASR] {text}")

        response = self.agent.respond(text)
        print(f"[Agent] {response}")

        self.tts.speak(response)

        self.player.play()



    def handle_interrupt(self):
        pass
