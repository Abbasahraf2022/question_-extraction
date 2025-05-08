import google.generativeai as genai
import json

# Configuration
API_KEY = "AIzaSyAYtrqUyWVR0kkgOqA58vW5JOn_jvsZlOo"  # Replace with your actual Gemini API key
IMAGE_PATH = "D:\\gen\\question_-extraction\\equat.jpg"  # Update to your image path

# Set up Gemini API
genai.configure(api_key=API_KEY)

# Read image bytes
with open(IMAGE_PATH, "rb") as f:
    img_bytes = f.read()

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Prompt
prompt = """
You are given an image containing handwritten steps for solving a quadratic equation.
Extract each step clearly and return the result in a JSON array of objects.
Each object should have:
- "step": the step number (starting from 1),
- "equation": the math expression or transformation written in that step.

Format:
[
  {"step": 1, "equation": "first equation"},
  {"step": 2, "equation": "second equation"},
  ...
]
Ensure all handwritten math steps are captured in correct sequence.
"""

# Generate content from image
response = model.generate_content(
    [
        {"text": prompt},
        {"inline_data": {"mime_type": "image/png", "data": img_bytes}},
    ]
)

# Print raw response
print("Raw Gemini Response:\n")
print(response.text)

# Try to parse and print JSON
print("\nParsed Step-by-Step Output:\n")
try:
    result = json.loads(response.text)
    for step in result:
        print(f"Step {step['step']}: {step['equation']}")
except json.JSONDecodeError:
    print("Could not parse the output as valid JSON. Please check the raw response.")
