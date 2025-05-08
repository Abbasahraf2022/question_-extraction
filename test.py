import google.generativeai as genai
import json

# Set your Gemini API Key
genai.configure(api_key="AIzaSyCw-5AWH-tUlpsWFoMTbvuZDwG8w_GeyZU")

# Load image bytes
image_path = "D:\\gen\\question_-extraction\\d1291b29-fc4f-4414-a3d7-87e852933c2e.jpeg"
with open(image_path, "rb") as f:
    img_bytes = f.read()

# Initialize the new model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Prompt
prompt = "Extract question numbers and their associated answers from this handwritten answer sheet. Return the results as a JSON list of objects with fields: question_number, question_box, answer_text, answer_box."

# Generate content with image and text
response = model.generate_content(
    [
        {"text": prompt},
        {"inline_data": {"mime_type": "image/jpeg", "data": img_bytes}}
    ]
)

# Print raw text output
print("Raw Gemini response:")
print(response.text)

# Try parsing JSON response
try:
    data = json.loads(response.text)
    print("\nParsed JSON output:")
    for item in data:
        print(f"Question: {item['question_number']}")
        print(f"Question Box: {item['question_box']}")
        print(f"Answer: {item['answer_text']}")
        print(f"Answer Box: {item['answer_box']}")
        print("-" * 40)
except json.JSONDecodeError:
    print("\nFailed to parse JSON. The model output might not be valid JSON.")
