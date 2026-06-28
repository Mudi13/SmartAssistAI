class MemoryService:

    conversation = []

    @staticmethod
    def add_user_message(message: str):
        MemoryService.conversation.append(
            {
                "role": "user",
                "content": message,
            }
        )
        
    @staticmethod
    def add_ai_message(message: str):
        MemoryService.conversation.append(
            {
                "role": "assistant",
                "content": message,
            }
        )
        
    @staticmethod
    def get_messages():
        return MemoryService.conversation