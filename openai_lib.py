import constants
from openai import OpenAI
import os
import utilities

client = OpenAI()
client.api_key = os.getenv('OPENAI_API_KEY') 

def chat(prompt, system_prompt):
    response = client.chat.completions.create(
        model=constants.OPENAI_MODEL,
        messages=
        [
            {
                "role" : "system", 
                "content": system_prompt
            },
            {
                "role" : "user", 
                "content" : prompt
            }
        ]
    )

    return response.choices[0].message.content

def look(prompt, image_path):
    image_response = client.chat.completions.create(
    model=constants.OPENAI_VISION_MODEL,
    messages = 
    [
        {
            "role": "user",
            "content": [
                {
                    "type": "text", "text": prompt
                },
                {
                    "type": "image", "image_url": 
                                    {
                                        "url": f"data:image/jpeg;base64,{utilities.encode_image(image_path)}"
                                    }
                }
            ]
        }
    ],
    max_tokens=1024
    )
    return image_response.choices[0].message.content

#converts audio to text using Whisper model
def transcribe(audio_file):
    return client.audio.transcriptions.create(
    model=constants.OPENAI_WHISPER_MODEL, 
    file=open(audio_file, "rb"),
    response_format="text"
    )

#Image generation
def generate_image(prompt):
    response = client.images.generate(
        model=constants.OPENAI_DALL_E,
        prompt=prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    return response.data[0].url