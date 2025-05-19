import os
import google.generativeai as genai

def get_fix(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-pro")
    print(f"✅ Using Gemini model: {model.model_name}")  # <-- debug print

    response = model.generate_content(prompt)
    return response.text.strip()
