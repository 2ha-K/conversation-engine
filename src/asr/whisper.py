from faster_whisper import WhisperModel
class WhisperASR:
    """快取要記得刪除"""
    def __init__(self):
        self.model = WhisperModel("small")

    def transcribe(self, audio):
        segments, _ = self.model.transcribe(audio.path)
        return "".join(segment.text for segment in segments)


