from openai import OpenAI
import os

def get_fix(prompt):
    """
    Sends the prompt to OpenAI GPT and returns the AI-suggested fix.
    """

    # Load your OpenAI API key from the environment
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise EnvironmentError("OPENAI_API_KEY not set in environment variables.")

    # Initialize OpenAI client
    client = OpenAI(api_key=api_key)

    # Send the prompt to the AI
    response = client.chat.completions.create(
        model="gpt-4",  # or "gpt-3.5-turbo" if you're on the free tier
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

    # Extract and return the AI's suggestion
    return response.choices[0].message.content.strip()
