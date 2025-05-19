import os
import google.generativeai as genai

def get_fix(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

    # Correct configuration
    genai.configure(api_key=api_key)

    # Use Gemini Pro with latest default (v1) API
    model = genai.GenerativeModel("gemini-pro")

    response = model.generate_content(prompt)
    return response.text.strip()
