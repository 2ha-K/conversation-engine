from google import genai
from models.base import BaseModel

class GeminiModel(BaseModel):

    def __init__(self, api_key: str):

        self.client = genai.Client(api_key=api_key)

    def generate(self, text: str) -> str:

        response = self.client.models.generate_content(
            model="gemini-3.5-flash",
            contents=text,
        )

        return response.text
