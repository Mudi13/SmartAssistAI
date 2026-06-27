from app.services.speech_service import SpeechService
from app.ai.services.ai_service import AIService

class VoiceService:

    @staticmethod
    def process_voice():
        audio_file = SpeechService.record_audio()
        
        if not audio_file:
            return None
        
        text = SpeechService.speech_to_text(audio_file)
        
        if not text:
            return None
        
        response = AIService.ask(text)
        speech_file = SpeechService.text_to_speech(response)
        
        if not speech_file:
            return None
        
        SpeechService.play_audio(speech_file)
        
        if not response:
            return None
        
        return response