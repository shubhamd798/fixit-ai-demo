import os
import re
import google.generativeai as genai

def get_fix(prompt, code_context):
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not set in environment variables.")

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")

    # 🔍 Log the prompt sent to Gemini
    print("🔍 Prompt sent to Gemini:")
    print("=" * 30)
    print(prompt)
    print("=" * 30)

    # 🔧 Generate fix from Gemini
    response = model.generate_content(prompt)
    fix = response.text.strip()

    # 🛡️ Validate that Gemini fixed the correct function
    match = re.search(r'def (\w+)\(', code_context['snippet'])
    if match:
        expected_func = match.group(1)
        if expected_func not in fix:
            raise ValueError(f"❌ Fix does not include original function: `{expected_func}`. Gemini output was:\n{fix}")

    return fix
