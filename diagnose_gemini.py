import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

print("\n🧠 Available Gemini models:")
for m in genai.list_models():
    supported = getattr(m, "supported_generation_methods", [])
    print(f"- {m.name} | supports: {supported}")
