import os
import re
import google.generativeai as genai

def get_fix(prompt):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    print("🔍 Prompt sent to Gemini:")
    print("=" * 30)
    print(prompt)
    print("=" * 30)

    response = model.generate_content(prompt)
    fix = response.text.strip()

    match = re.search(r'def (\w+)\(', prompt)
    if match:
        expected_func = match.group(1)
        if expected_func not in fix:
            raise ValueError(f"❌ Fix does not include original function: `{expected_func}`. Gemini output was:\n{fix}")

    return fix
