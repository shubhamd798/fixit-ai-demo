import os
import google.generativeai as genai

def get_fix(prompt):
    # Load API key from environment
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

    # Configure Gemini
    genai.configure(api_key=api_key)

    # Choose a stable supported model
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    # 🔍 Debug: Print the prompt being sent to Gemini
    print("🔍 Prompt sent to Gemini:")
    print("=" * 30)
    print(prompt)
    print("=" * 30)

    # Generate fix
    response = model.generate_content(prompt)
    return response.text.strip()
