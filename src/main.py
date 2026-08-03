from orchestrator.orchestrator import ASR, TTS, ConversationOrchestrator, Agent
from asr.whisper import WhisperASR
from agent.selector.brain_selector import BrainSelector
from agent.brains.fast.brain import FastBrain


asr = ASR(WhisperASR())
selector = BrainSelector(fast_brain=FastBrain(), medium_brain=None, slow_brain=None)
agent = Agent(selector=selector)
tts = TTS()

engine = ConversationOrchestrator(
    asr,
    agent,
    tts
)

engine.handle_conversation()