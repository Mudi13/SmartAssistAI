from app.services.speech_service import SpeechService
from app.ai.services.ai_service import AIService
import os

class VoiceService:
    
    @staticmethod
    def process_voice():
        try:
            print("🎤 Recording... Speak now!")
            audio_file = SpeechService.record_audio()
            
            if not audio_file:
                return None
            
            print("📝 Converting speech to text...")
            text = SpeechService.speech_to_text(audio_file)
            
            if not text:
                print("⚠️ No text detected from speech.")
                return None

            print("🤖 Thinking...")
            response = AIService.ask(text)

            if not response:
                print("❌ AIService returned an empty response.")
                return None

            print("🔊 Generating speech...")
            speech_file = SpeechService.text_to_speech(response)

            if not speech_file:
                return None

            print("🔈 Playing response...")
            SpeechService.play_audio(speech_file)
            
            try:
                if os.path.exists(audio_file):
                    os.remove(audio_file)

                if os.path.exists(speech_file):
                    os.remove(speech_file)

            except Exception as e:
                print(f"⚠️ Cleanup failed: {e}")
                
                
            print("✅ Conversation completed.")
            
            return {
                "user_text": text,
                "ai_response": response,
                "success": True,
            }

        except Exception as e:
            print(f"❌ Voice conversation failed: {e}")
            return {
                "success": False,
                "message": str(e)
            }