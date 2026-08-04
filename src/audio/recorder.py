from pathlib import Path
import sounddevice as sd
import soundfile as sf
from audio.data import AudioData

class Recorder:
    SAMPLE_RATE = 16000 #Sample Rate（取樣率）就是一秒鐘取幾次樣本（Sample）
    CHANNELS = 1 #聲道

    def show_devices(self):
        input_id, _ = sd.default.device
        device = sd.query_devices(input_id)
        if device["max_input_channels"] == 0:
            raise RuntimeError("No microphone detected.")
        print(f"Using microphone: {device['name']}")



    def record(self, duration: int = 5) -> AudioData:
        """
        Record audio and return AudioData.
        """
        output_path = Path("data/audio/input/temp.wav")
        print(f"Recording {duration} seconds...")

        audio = sd.rec(
            int(duration * self.SAMPLE_RATE),
            samplerate=self.SAMPLE_RATE,
            channels=self.CHANNELS,
            dtype="float32",
        )

        sd.wait() #因為 sd.rec() 是非同步（Asynchronous）

        output_path.parent.mkdir(parents=True, exist_ok=True)

        sf.write(output_path, audio, self.SAMPLE_RATE, subtype="PCM_16")

        print("Recording finished.")

        return AudioData(path=output_path)