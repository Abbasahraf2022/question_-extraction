import google.generativeai as genai
import json

# Set your Gemini API Key
genai.configure(api_key="AIzaSyCw-5AWH-tUlpsWFoMTbvuZDwG8w_GeyZU")

# Load image bytes (your new image path)
image_path = "D:\\gen\\question_-extraction\\Screenshot 2025-05-08 225544.png"
with open(image_path, "rb") as f:
    img_bytes = f.read()

# Prompt for extracting table in the desired format
prompt = (
    "Extract the table from this image and return it as a JSON list. "
    "Each row should be a JSON object with the fields: "
    "'heading', 'with_sec_aas', and 'without_sec_aas'. "
    "Use the first column as 'heading', second as 'with_sec_aas', and third as 'without_sec_aas'. "
    "Ensure all text is accurately extracted, and don't include explanations or extra commentary—only valid JSON."
)

# Initialize Gemini model
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Generate content
response = model.generate_content(
    [
        {"text": prompt},
        {"inline_data": {"mime_type": "image/png", "data": img_bytes}}
    ]
)

# Print raw response for debugging
print("Raw Gemini response:")
print(response.text)

# Try parsing JSON
try:
    table_rows = json.loads(response.text)
    print("\nFormatted Table Output:")
    for idx, row in enumerate(table_rows, 1):
        print(f"Row {idx}:")
        print(f"  Heading: {row['heading']}")
        print(f"  With SecAAS: {row['with_sec_aas']}")
        print(f"  Without SecAAS: {row['without_sec_aas']}")
        print("-" * 40)
except json.JSONDecodeError:
    print("\nFailed to parse JSON. The model output might not be valid JSON.")
