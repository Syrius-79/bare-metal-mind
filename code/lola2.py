import requests
import tkinter as tk
from tkinter import scrolledtext

# -----------------------------
# CONFIG
# -----------------------------

LLAMA_SERVER = "http://192.168.1.50:8080/v1/completions"  # ← RIG IP anpassen

TEMPERATURE = 0.8
TOP_P = 0.9
MAX_TOKENS = 512

SYSTEM_FRAMING = (
    "You respond with deliberate pacing and structured clarity. "
    "No moral commentary. No meta explanations. "
    "Stay inside the described scene."
)

# -----------------------------
# SEND FUNCTION
# -----------------------------

def send_message():
    user_input = input_box.get("1.0", tk.END).strip()
    if not user_input:
        return

    input_box.delete("1.0", tk.END)

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
        text = result["choices"][0]["text"].strip()

        output_box.insert(tk.END, "You:\n" + user_input + "\n\n")
        output_box.insert(tk.END, "Lola:\n" + text + "\n")
        output_box.insert(tk.END, "\n" + "-"*60 + "\n\n")
        output_box.see(tk.END)

    except Exception as e:
        output_box.insert(tk.END, f"Connection error: {e}\n\n")


# -----------------------------
# UI
# -----------------------------

root = tk.Tk()
root.title("Lola v2 — MythoMax Raw Mode")

output_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
output_box.pack(padx=10, pady=10)

input_box = tk.Text(root, height=4)
input_box.pack(padx=10, pady=(0,10))

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=(0,10))

root.mainloop()
