import google.generativeai as genai
import os
import constants
import PIL.Image

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def chat(prompt):
    model = genai.GenerativeModel(constants.GOOGLE_MODEL)
    response = model.generate_content(prompt)
    return response.candidates[0].content.parts[0].text

def look(question, image_path):
    model = genai.GenerativeModel(constants.GOOGLE_VISION_MODEL)
    img = PIL.Image.open(image_path)
    response = model.generate_content([question, img])
    return response.candidates[0].content.parts[0].text
    