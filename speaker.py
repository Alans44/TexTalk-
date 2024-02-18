import requests
from dotenv import load_dotenv, find_dotenv
import os
import soundfile as sf
from IPython.display import Audio
import numpy as np
import torch

load_dotenv(find_dotenv())

API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
HF_API_KEY = os.getenv("HF_API_KEY")
headers = {"Authorization": f"Bearer {HF_API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response
	

def tts(text, index):
	audio = query({
		"inputs": text,
	})
	with open(f"resources/more/.speech{index}.wav", "wb") as f:
		f.write(audio.content)
	return audio.content
