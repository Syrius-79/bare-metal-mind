import requests
import tkinter as tk
import json

with open("config.json") as f:
    config = json.load(f)

with open("prompt.txt") as f:
    SYSTEM_FRAMING = f.read().strip()

def send():
    user_input = entry.get("1.0", tk.END).strip()
    full_prompt = SYSTEM_FRAMING + "\n\n" + user_input

    payload = {
        "prompt": full_prompt,
        "temperature": temp_scale.get(),
        "top_p": top_p_scale.get(),
        "max_tokens": int(max_tokens_entry.get())
    }

    try:
        r = requests.post(config["server"], json=payload)
        result = r.json()
        output.insert(tk.END, "\nLola:\n" + result["choices"][0]["text"].strip() + "\n")
    except Exception as e:
        output.insert(tk.END, f"\nError: {e}\n")

root = tk.Tk()
root.title("LOLA5 — RIG Superbomb Control")

entry = tk.Text(root, height=5, width=80)
entry.pack()

temp_scale = tk.Scale(root, from_=0.1, to=1.5, resolution=0.1,
                      orient=tk.HORIZONTAL, label="Temperature")
temp_scale.set(config["temperature"])
temp_scale.pack()

top_p_scale = tk.Scale(root, from_=0.1, to=1.0, resolution=0.05,
                       orient=tk.HORIZONTAL, label="Top-P")
top_p_scale.set(config["top_p"])
top_p_scale.pack()

max_tokens_entry = tk.Entry(root)
max_tokens_entry.insert(0, config["max_tokens"])
max_tokens_entry.pack()

btn = tk.Button(root, text="Send", command=send)
btn.pack()

output = tk.Text(root, height=20, width=80)
output.pack()

root.mainloop()
