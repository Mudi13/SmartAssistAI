from openai import OpenAI
from app.core.config import settings
from app.ai.prompts.system_prompt import SYSTEM_PROMPT
import base64

client = OpenAI(api_key=settings.OPENAI_API_KEY)


class AIService:

    @staticmethod
    def ask(messages):
        response = client.responses.create(
            model=settings.MODEL,
            instructions=SYSTEM_PROMPT,
            input=messages,
        )

        return response.output_text

    @staticmethod
    def analyze_image(image_path: str):
        try:
            with open(image_path, "rb") as image:
                image_data = image.read()
                base64_image = base64.b64encode(image_data).decode("utf-8")

            response = client.responses.create(
                model=settings.MODEL,
                instructions=SYSTEM_PROMPT,
                input=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "input_text",
                                "text": "Analyze this image and describe everything you can see.",
                            },
                            {
                                "type": "input_image",
                                "image_url": f"data:image/png;base64,{base64_image}",
                            },
                        ],
                    }
                ],
            )

            return response.output_text

        except Exception as e:
            print(f"Error analyzing image: {e}")
            return None