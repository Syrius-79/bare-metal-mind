import requests

LLAMA_SERVER = "http://192.168.1.50:8080/v1/completions"

TEMPERATURE = 0.8
TOP_P = 0.9
MAX_TOKENS = 512

print("Lola1 — Bare Metal Mode")
print("Type /exit to quit.\n")

while True:
    user_input = input("You> ")

    if user_input.strip().lower() == "/exit":
        break

    payload = {
        "prompt": user_input,
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
