import requests
import os
import dotenv
dotenv.load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2-1"
headers = {"Authorization": "Bearer "+os.environ.get('HF_TOKEN')}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

def igen(prompt):
    return query({
        "inputs": prompt,
    })

import io
from PIL import Image

def img(prompt):
    return Image.open(io.BytesIO(igen(prompt)))
