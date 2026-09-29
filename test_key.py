import os

key = os.getenv("GEMINI_API_KEY")

if key:
    print("API key found!")
else:
    print("API key not found!")