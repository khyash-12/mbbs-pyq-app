import requests
import base64
import os

API_KEY = os.environ.get("GEMINI_API_KEY")
print("Gemini key loaded:", API_KEY)

def extract_questions_from_pdf(pdf_path):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

    with open(pdf_path, "rb") as f:
        pdf_bytes = f.read()

    encoded_pdf = base64.b64encode(pdf_bytes).decode("utf-8")

    prompt = """
You are reading a medical university exam question paper.

Extract ALL exam questions from this document.

Rules:
- Ignore headings
- Ignore instructions
- Ignore star ratings or formatting symbols
- Return only the questions
- Return them as a numbered list
"""

    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt},
                    {
                        "inline_data": {
                            "mime_type": "application/pdf",
                            "data": encoded_pdf
                        }
                    }
                ]
            }
        ]
    }

    response = requests.post(url, json=payload)

    result = response.json()

    try:
        return result["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return str(result)