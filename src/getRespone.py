"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import PIL.Image
import google.generativeai as genai

# genai.configure(api_key=os.environ["GEMINI_API_KEY"])
genai.configure(api_key="Your_API")

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

def save_file(content, path):
    with open(path, "w") as f:
        f.write(content)

def getRes(path_img):
  prompt = "Chuyển mọi chi tiết, từ các chi tiết nhỏ nhất như màu sắc, vị trí, kiểu,... sang 2 file html và css"
  img = PIL.Image.open(path_img)
  response = model.generate_content([prompt, img])
  return response.text

