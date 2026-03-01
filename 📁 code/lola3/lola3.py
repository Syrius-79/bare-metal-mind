import requests
import os

LLAMA_SERVER = "http://192.168.1.50:8080/v1/completions"

PROMPT_FILE = "prompt.txt"

TEMPERATURE = 0.8
TOP_P = 0.9
MAX_TOKENS = 512

def load_prompt():
    if not os.path.exists(PROMPT_FILE):
        print("Prompt file missing.")
        exit()
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()

SYSTEM_FRAMING = load_prompt()

print("LOLA3 — External Prompt Mode (RIG Active)\n")

while True:
    user_input = input("You> ")

    if user_input.lower() == "/exit":
        break

    full_prompt = SYSTEM_FRAMING + "\n\n" + user_input

    payload = {
        "prompt": full_prompt,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": MAX_TOKENS
    }

    try:
        r = requests.post(LLAMA_SERVER, json=payload)
        result = r.json()
        print("\nLola>\n")
        print(result["choices"][0]["text"].strip())
        print("\n" + "-"*50 + "\n")
    except Exception as e:
        print("Connection error:", e)
