from openai import OpenAI
import os

def get_fix(prompt):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set in environment variables.")

    client = OpenAI(api_key=api_key)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # <-- this is the fix
        messages=[
            {
                "role": "system",
                "content": "You are an expert Python developer. Fix the user's broken code with clean, minimal edits."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
