# fixit_ai/utils/config.py

import os
from dotenv import load_dotenv

# Load from .env file in root
load_dotenv()

# === OpenAI ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "gpt-4")

# === GitHub ===
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_REPO = os.getenv("GITHUB_REPO")  # e.g. shubhamd798/fixit-ai-demo
GITHUB_BRANCH = os.getenv("GITHUB_BRANCH", "fixit-ai-bot-patch")

# === Git Config ===
GIT_AUTHOR_NAME = os.getenv("GIT_AUTHOR_NAME", "FixItAI Bot")
GIT_AUTHOR_EMAIL = os.getenv("GIT_AUTHOR_EMAIL", "fixitai@example.com")
