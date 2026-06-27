from app.services.speech_service import SpeechService

audio = SpeechService.record_audio()

text = SpeechService.speech_to_text(audio)

print(text)