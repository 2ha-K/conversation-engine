# test/test_brain.py
import os
from dotenv import load_dotenv
from agent.brains.fast.brain import FastBrain
from models.gemini import GeminiModel

def test_brain_response():
    load_dotenv()
    brain = FastBrain(GeminiModel(os.getenv("GEMINI_API_KEY")))
    response = brain.respond("你好")
    print(response)
    assert response is not None