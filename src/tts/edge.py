import asyncio
import edge_tts

from tts.base import TTS
from audio.pydub_coonverter import PydubConverter
from audio.converter import AudioConverter

OUTPUT_MP3_PATH="data/audio/output/tts.mp3"

class EdgeTTS(TTS):
    def __init__(self, converter: AudioConverter):
        self.converter = converter

    VOICE = "zh-TW-HsiaoChenNeural"

    async def _speak(self, text: str): #非同步函式（Coroutine）。它不能直接呼叫
        communicate = edge_tts.Communicate(
            text=text,
            voice=self.VOICE
        ) #建立一個 TTS 工作

        await communicate.save(OUTPUT_MP3_PATH) #向 Edge TTS Api要求合成語音，並存成檔案 (遇到需要等待的工作時，把控制權交回 Event Loop)

    def speak(self, text: str) -> None:
        """建立一個 Event Loop，把 _speak() 執行完，再關閉 Event Loop。"""
        asyncio.run(self._speak(text)) #asyncio.run()：建立 Event Loop，開始執行 async 程式。
        return self.converter.to_wav(
            input_path=OUTPUT_MP3_PATH,
            output_path=OUTPUT_MP3_PATH.replace(".mp3", ".wav")
        )