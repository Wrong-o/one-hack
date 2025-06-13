from fastapi import FastAPI
from typing import List, Dict
import openai
from os import getenv


api_key = getenv("OPENAI_API_KEY")
app = FastAPI()


@app.post("/")
def get_chat(participant: str, chat_history = List[Dict[str,str]]) -> str:
    print("Hello")
    return "hello"






if __name__ == "__main__":
    get_chat()
