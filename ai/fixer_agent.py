import os
import google.generativeai as genai

def get_fix(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

    # ✅ Use the correct API version
    genai.configure(api_key=api_key, transport="rest")  # important for GitHub runners

    # ✅ Use the correct model
    model = genai.GenerativeModel(model_name="models/gemini-pro")

    response = model.generate_content(prompt)
    return response.text.strip()
