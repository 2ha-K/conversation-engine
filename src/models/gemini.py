from google import genai
from models.base import BaseModel

class GeminiModel(BaseModel):

    def __init__(self, api_key: str):

        self.client = genai.Client(api_key=api_key)

    def generate(self, text: str) -> str:
        try:
            response = self.client.models.generate_content(
                model="gemini-3.5-flash",
                contents=text,
            )
        except Exception as e:
            print(f"[Gemini Error] {e}")
            return "抱歉，目前 AI 無法回應。"

        return response.text
