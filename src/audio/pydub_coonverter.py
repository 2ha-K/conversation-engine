from pathlib import Path

from pydub import AudioSegment

from audio.converter import AudioConverter


class PydubConverter(AudioConverter):

    def to_wav(self, input_path: Path, output_path: Path) -> Path:
        audio = AudioSegment.from_file(input_path)
        audio.export(output_path, format="wav")
        return output_path