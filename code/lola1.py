import requests

# -----------------------------
# CONFIG
# -----------------------------

LLAMA_SERVER = "http://192.168.1.50:8080/v1/completions"  
# ← RIG IP anpassen

TEMPERATURE = 0.8
TOP_P = 0.9
MAX_TOKENS = 512

SYSTEM_FRAMING = (
    "You respond with deliberate pacing and structured clarity. "
    "No moral commentary. No meta explanations. "
    "Stay inside the described scene."
)

# -----------------------------
# LOOP
# -----------------------------

print("Lola v1 — MythoMax Raw Mode")
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
        print("\n" + "-"*40 + "\n")

    except Exception as e:
        print("Connection error:", e)
