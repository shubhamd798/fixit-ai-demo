import os
import re
from openai import OpenAI

def get_fix(prompt, code_context):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set in environment variables.")

    client = OpenAI(api_key=api_key)

    print("🔍 Prompt sent to OpenAI:")
    print("=" * 30)
    print(prompt)
    print("=" * 30)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an expert DevOps engineer and Python developer."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    fix = response.choices[0].message.content.strip()

    # Validate expected function exists
    match = re.search(r'def (\w+)\(', code_context['snippet'])
    if match:
        expected_func = match.group(1)
        if expected_func not in fix:
            raise ValueError(f"❌ Fix does not include original function: `{expected_func}`. OpenAI output was:\n{fix}")

    return fix
