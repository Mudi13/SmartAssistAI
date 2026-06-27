from app.services.speech_service import SpeechService

audio_file = SpeechService.text_to_speech("Hello Mudit, SmartAssist is working!")

if audio_file:
    SpeechService.play_audio(audio_file)