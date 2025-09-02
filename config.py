import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("⚠️ OPENAI_API_KEY not found. Please set it before running.")

