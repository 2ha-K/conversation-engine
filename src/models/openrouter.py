from openai import OpenAI, OpenAIError
from models.base import BaseModel


class OpenRouterModel(BaseModel):

    def __init__(self, api_key: str):
        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1",
        )

    def generate(self, text: str) -> str:
        try:
            response = self.client.chat.completions.create(
                model="openrouter/free",   # 之後可以換成其他模型
                messages=[
                    {
                        "role": "user",
                        "content": text,
                    }
                ],
            )
        except OpenAIError as e:
            print(f"[OpenRouter Error] {e}")
            return "抱歉，目前 AI 無法回應。"

        return response.choices[0].message.content