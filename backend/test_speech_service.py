from app.services.voice_service import VoiceService

while True:
    response = VoiceService.process_voice()

    print(response)