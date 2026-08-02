from faster_whisper import WhisperModel

class WhisperASR:
    """快取要記得刪除"""
    def __init__(self):
        self.model = WhisperModel("small")

    def transcribe(self, audio_path):
        segments, _ = self.model.transcribe(audio_path)
        return "".join(segment.text for segment in segments)

if __name__ == "__main__":
    asr = WhisperASR()
    audio_path = "tests/assets/audio/test_audio01.mp3"  # Replace with your audio file path
    transcription = asr.transcribe(audio_path)
    print("Transcription:", transcription)

