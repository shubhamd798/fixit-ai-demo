import os
import google.generativeai as genai

def get_fix(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

    genai.configure(api_key=api_key)

    # Use a stable, supported model
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    response = model.generate_content(prompt)
    return response.text.strip()
