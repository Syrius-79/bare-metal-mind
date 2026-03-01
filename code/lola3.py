import requests
import os

# -----------------------------
# CONFIG
# -----------------------------

LLAMA_SERVER = "http://192.168.1.50:8080/v1/completions"  # RIG IP anpassen
PROMPT_FILE = "lola_prompt.txt"

TEMPERATURE = 0.8
TOP_P = 0.9
MAX_TOKENS = 512


# -----------------------------
# LOAD PROMPT
# -----------------------------

def load_prompt():
    if not os.path.exists(PROMPT_FILE):
        print("Prompt file not found:", PROMPT_FILE)
        exit(1)

    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


SYSTEM_FRAMING = load_prompt()


# -----------------------------
# LOOP
# -----------------------------

print("Lola v3 — MythoMax Raw Mode (External Prompt)")
print("Type /exit to quit.\n")

while True:
    user_input = input("You> ")

    if user_input.strip().lower() == "/exit":
        break

    full_prompt = SYSTEM_FRAMING + "\n\n" + user_input

    payload = {
        "prompt": full_prompt,
        "temperature": TEMPERATURE,
        "top_p": TOP_P,
        "max_tokens": MAX_TOKENS,
        "stream": False
    }

    try:
        response = requests.post(LLAMA_SERVER, json=payload)
        result = response.json()
        text = result["choices"][0]["text"]

        print("\nLola>\n")
        print(text.strip())
        print("\n" + "-"*50 + "\n")

    except Exception as e:
        print("Connection error:", e)
