from orchestrator.orchestrator import ASR, LLM, TTS, ConversationOrchestrator, Memory


asr = ASR()
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