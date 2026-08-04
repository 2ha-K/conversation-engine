from orchestrator.orchestrator import ASR, TTS, ConversationOrchestrator, Agent
from asr.whisper import WhisperASR
from agent.selector.brain_selector import BrainSelector
from agent.brains.fast.brain import FastBrain
from models.gemini import GeminiModel
from dotenv import load_dotenv
import os

load_dotenv()

asr = ASR(WhisperASR())
model = GeminiModel(api_key=os.getenv("GEMINI_API_KEY"))
fast_brain = FastBrain(model=model)
selector = BrainSelector(fast_brain=fast_brain, medium_brain=None, slow_brain=None)
agent = Agent(selector=selector)
tts = TTS()

engine = ConversationOrchestrator(
    asr,
    agent,
    tts
)

engine.handle_conversation()