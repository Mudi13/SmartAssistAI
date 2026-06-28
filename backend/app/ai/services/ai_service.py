from openai import OpenAI
from app.core.config import settings
from app.ai.prompts.system_prompt import SYSTEM_PROMPT

client = OpenAI(api_key= settings.OPENAI_API_KEY)

class AIService:
    @staticmethod
    def ask(user_message: str):
        response = client.chat.completions.create(
            model = settings.MODEL,
            messages=[
                {
                    "role": "system", 
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user", 
                    "content": user_message
                },   
            ],
        )

        return response.choices[0].message.content