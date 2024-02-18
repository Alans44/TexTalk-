import requests
from dotenv import load_dotenv, find_dotenv
import os
import llm_bridge

load_dotenv(find_dotenv())

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
HF_API_KEY = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

def audio_to_latex(filename): 
    print("Sending to api...")
    output = query(filename)
    print(output['text'])
    prompt = llm_bridge.build_prompt_latex(output["text"])
    res = llm_bridge.get_response("gpt-4", prompt)
    print(res)
    return res
