import os
import openai
import google.generativeai as genai
from dotenv import load_dotenv

# Force reload of .env
load_dotenv(override=True)

o_key = os.getenv("OPEN_AI_KEY")
g_key = os.getenv("GEMINI_AI_KEY")

def parse_error(e):
    return str(e).split('\n')[0]

print("--- DIAGNOSTICS ---")
print(f"OpenAI Key Loaded: {bool(o_key)} - Ends with: {o_key[-4:] if o_key else 'None'}")
print(f"Gemini Key Loaded: {bool(g_key)} - Ends with: {g_key[-4:] if g_key else 'None'}")
print("-------------------")

# Test OpenAI
if o_key:
    print("\nTesting OpenAI...")
    try:
        client = openai.OpenAI(api_key=o_key)
        # Just try to list models to check auth
        client.models.list()
        print("[OK] OpenAI Auth: SUCCESS")
    except Exception as e:
        print(f"[FAIL] OpenAI Auth: FAILED - {parse_error(e)}")
else:
    print("[SKIP] OpenAI: SKIPPED (No Key)")

# Test Gemini
if g_key:
    print("\nTesting Gemini 1.5 Flash...")
    try:
        genai.configure(api_key=g_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("Hello")
        print("[OK] Gemini Auth: SUCCESS")
    except Exception as e:
        print(f"[FAIL] Gemini Auth: FAILED - {parse_error(e)}")
        
    print("\nTesting Gemini 1.5 Pro (Fallback)...")
    try:
        model = genai.GenerativeModel('gemini-1.5-pro')
        response = model.generate_content("Hello")
        print("[OK] Gemini Pro Auth: SUCCESS")
    except Exception as e:
        print(f"[FAIL] Gemini Pro Auth: FAILED - {parse_error(e)}")
else:
    print("[SKIP] Gemini: SKIPPED (No Key)")
