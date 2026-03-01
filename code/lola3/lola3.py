import requests
import os

# --- RIG SERVER (4 GPUs obviously) ---
LLAMA_SERVER = "http://192.168.1.50:8080/v1/completions"

# --- Settings ---
TEMPERATURE = 0.8
TOP_P = 0.9
MAX_TOKENS = 512

PROMPT_FILE = "prompt.txt"


def load_prompt():
    if not os.path.exists(PROMPT_FILE):
        print("prompt.txt not found.")
        exit()
    with open(PROMPT_FILE, "r", encoding="utf-8") as f:
        return f.read().strip()


SYSTEM_PROMPT = load_prompt()

print("LOLA3 — External Prompt Mode (RIG Online)")
print("Type /exit to quit.\n")


while True:
    user_input = input("You> ").strip()

    if user_input.lower() == "/exit":
        break

    full_prompt = SYSTEM_PROMPT + "\n\n" + user_input

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
        print("\n" + "-" * 60 + "\n")

    except Exception as e:
        print("Connection error:", e)
