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