import sounddevice as sd
import soundfile as sf
import numpy as np
from faster_whisper import WhisperModel


class SpeechService:
    SAMPLE_RATE = 44100
    CHANNELS = 1
    DTYPE = "float32"

    MODEL = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

    @staticmethod
    def record_audio(duration: int = 5, filename: str = "voice.wav"):
        """
        Record audio from the default microphone.

        Args:
            duration (int): Recording duration in seconds.
            filename (str): Output WAV file name.

        Returns:
            str | None: Path to the recorded audio file or None if recording fails.
        """

        try:
            print("🎤 Recording... Speak now!")

            audio = sd.rec(
                int(duration * SpeechService.SAMPLE_RATE),
                samplerate=SpeechService.SAMPLE_RATE,
                channels=SpeechService.CHANNELS,
                dtype=SpeechService.DTYPE,
            )

            sd.wait()

            # Normalize volume
            max_amplitude = np.max(np.abs(audio))

            if max_amplitude > 0:
                audio = audio / max_amplitude * 0.9

            sf.write(filename, audio, SpeechService.SAMPLE_RATE)

            print(f"✅ Recording completed.")
            print(f"💾 Audio saved as {filename}")

            return filename

        except Exception as e:
            print(f"❌ Recording failed: {e}")
            return None
        
        
    #Speech to Text (STT)
    @staticmethod
    def speech_to_text(audio_path: str):
        try:
            segments, info = SpeechService.MODEL.transcribe(
                audio_path,
                beam_size = 5,
                vad_filter=True
            )
            
            text = " ".join(segment.text for segment in segments).strip()
            
            if not text:
                print("⚠️ No speech detected.")
                return None
                
            return text
        
   
        except Exception as e:
            print(f"❌ Speech recognition failed: {e}")
            return None