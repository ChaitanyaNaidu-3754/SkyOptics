import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

# Force reload of .env
load_dotenv(override=True)

o_key = os.getenv("OPEN_AI_KEY")
g_key = os.getenv("GEMINI_AI_KEY")

print("--- MODEL DISCOVERY ---")

# OpenAI Discovery
if o_key:
    print("\n[OpenAI] Fetching available models...")
    try:
        client = openai.OpenAI(api_key=o_key)
        models = client.models.list()
        # Filter for chat models to keep output clean
        chat_models = [m.id for m in models.data if 'gpt' in m.id]
        print(f"Found {len(chat_models)} GPT models:")
        for m in sorted(chat_models):
            print(f" - {m}")
    except Exception as e:
        print(f"OpenAI Error: {e}")
else:
    print("OpenAI Key missing.")

# Gemini Discovery
if g_key:
    print("\n[Gemini] Fetching available models...")
    try:
        genai.configure(api_key=g_key)
        models = genai.list_models()
        print("Found Gemini models:")
        for m in models:
            if 'generateContent' in m.supported_generation_methods:
                print(f" - {m.name}")
    except Exception as e:
        print(f"Gemini Error: {e}")
else:
    print("Gemini Key missing.")
