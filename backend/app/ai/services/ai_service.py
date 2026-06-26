from openai import OpenAI
from app.core.config import Settings
from app.ai.prompts.system_prompt import SYSTEM_PROMPT

client = OpenAI(api_key= Settings.OPENAI_API_KEY)

def chat(user_message: str):
    response = client.chat.completions.create(
        model = Settings.MODEL,
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