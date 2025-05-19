import openai
from utils.config import OPENAI_API_KEY, DEFAULT_MODEL

openai.api_key = OPENAI_API_KEY

def get_fix(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model=DEFAULT_MODEL,
            messages=[
                {"role": "system", "content": "You are an expert software engineer."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"AI failed to provide fix: {str(e)}"