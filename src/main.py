from orchestrator.orchestrator import ConversationOrchestrator
from agent.base import Agent
from audio.pydub_coonverter import PydubConverter
from tts.edge import EdgeTTS as TTS
from asr.whisper import WhisperASR
from agent.selector.brain_selector import BrainSelector
from agent.brains.fast.brain import FastBrain
from models.gemini import GeminiModel
from dotenv import load_dotenv
from players.simple_player import SimplePlayer
import os
from audio.recorder import Recorder
from models.openrouter import OpenRouterModel

load_dotenv()

asr = WhisperASR()
# model = GeminiModel(api_key=os.getenv("GEMINI_API_KEY"))
model = OpenRouterModel(api_key=os.getenv("OPENROUTER_API_KEY"))
fast_brain = FastBrain(model=model)
selector = BrainSelector(fast_brain=fast_brain, medium_brain=None, slow_brain=None)
agent = Agent(selector=selector)
tts = TTS(converter=PydubConverter())
player=SimplePlayer()

engine = ConversationOrchestrator(
    asr,
    agent,
    tts,
    player
)
    
recorder = Recorder()
recorder.show_devices()
audio = recorder.record(10)
engine.handle_conversation(audio)