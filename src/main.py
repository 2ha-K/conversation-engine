from orchestrator.orchestrator import ASR, LLM, TTS, ConversationOrchestrator, Memory
from asr.whisper import WhisperASR


asr = ASR(WhisperASR())
memory = Memory()
llm = LLM()
tts = TTS()

engine = ConversationOrchestrator(
    asr,
    memory,
    llm,
    tts
)

engine.handle_conversation()