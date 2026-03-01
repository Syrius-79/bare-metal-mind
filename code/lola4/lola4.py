import requests
import tkinter as tk

LLAMA_SERVER = "http://192.168.1.50:8080/v1/completions"

TEMPERATURE = 0.8
TOP_P = 0.9
MAX_TOKENS = 512

SYSTEM_FRAMING = "Respond clearly. Stay in scene."

def send():
    user_input = entry.get()
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
        output.insert(tk.END, "\nLola:\n" + result["choices"][0]["text"].strip() + "\n")
    except Exception as e:
        output.insert(tk.END, f"\nError: {e}\n")

root = tk.Tk()
root.title("LOLA4 — RIG Control Panel")

entry = tk.Entry(root, width=80)
entry.pack()

btn = tk.Button(root, text="Send", command=send)
btn.pack()

output = tk.Text(root, height=20, width=80)
output.pack()

root.mainloop()
