from orchestrator.orchestrator import ASR, TTS, ConversationOrchestrator, Agent
from asr.whisper import WhisperASR
from agent.selector.brain_selector import BrainSelector
from agent.brains.fast.brain import FastBrain
from models.gemini import GeminiModel
from dotenv import load_dotenv
import os
import time
from audio.data import AudioData

start = time.perf_counter()

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

audio = AudioData(path="tests/assets/audio/test_audio01.mp3")
engine.handle_conversation(audio)


end = time.perf_counter()
print(f"Total execution time: {end - start:.2f} seconds")