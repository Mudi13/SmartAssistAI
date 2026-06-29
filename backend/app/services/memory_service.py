class MemoryService:

    conversation = []
    
    MAX_MESSAGES = 20

    @staticmethod
    def add_user_message(message: str):
        MemoryService.conversation.append(
            {
                "role": "user",
                "content": message,
            }
        )
        MemoryService.trim_memory()
        
    @staticmethod
    def add_ai_message(message: str):
        MemoryService.conversation.append(
            {
                "role": "assistant",
                "content": message,
            }
        )
        MemoryService.trim_memory()
    @staticmethod
    def get_messages():
        return MemoryService.conversation
    
    @staticmethod
    def clear_memory():
        MemoryService.conversation.clear()
    
    @staticmethod
    def trim_memory():
        if len(MemoryService.conversation) > MemoryService.MAX_MESSAGES:
            MemoryService.conversation = MemoryService.conversation[-MemoryService.MAX_MESSAGES:]