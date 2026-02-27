---
layout: post
title: "Uncensored LLM on Windows in 20 Minutes"
---
# LLM Studio vs llama.cpp
## What you’re actually running on your PC

Most people think AI means ChatGPT.

It doesn’t.

ChatGPT is a cloud service.
A company runs it.
They control it.
They filter it.

A local LLM is different.

It runs on YOUR machine.
On YOUR hardware.
Under YOUR control.

That’s the difference.

---

## First: What is an LLM?

LLM = Large Language Model.

It’s just a very big prediction machine.

You give it text.
It predicts the next word.
Then the next.
Then the next.

That’s it.

No feelings.
No opinions.
No morality.

Just probability.

---

## What is GGUF?

When you download a local model, you’ll see a file ending in:

.gguf

That file contains:
- The trained weights (the “brain”)
- The vocabulary
- The rules for tokenization

Think of it as:
The compressed brain file.

No internet required.
No account required.

---

## What does Q4_K_M mean?

You’ll see model names like:

mistral-7b-instruct.Q4_K_M.gguf

Break it down:

7B = 7 billion parameters (size of the brain)

Q4 = 4-bit quantization  
That means the model was compressed to use less memory.

Smaller number → less memory  
But slightly lower quality.

K_M = a specific compression method  
Usually better than older Q4 versions.

Translation:
Q4_K_M is a good balance between quality and speed.

If your PC has limited RAM or VRAM,
this matters.

---

## What does “uncensored” mean?

There is no magic uncensored switch.

Models are trained in stages:

1. Base model  
   Raw language ability.

2. Instruct model  
   Fine-tuned to behave “helpfully”.

3. Safety-tuned model  
   Fine-tuned to avoid certain topics.

When people say “uncensored”,
they usually mean:

Less safety fine-tuning.

It does NOT mean:
Infinite freedom.
Infinite intelligence.
No limits.

The architecture still limits behavior.

---

## LLM Studio

LLM Studio is a graphical interface.

It hides complexity.

You:
- Download model
- Click start
- Move sliders

It works.
And for many people, that’s enough.

But you don’t see:
- Memory usage
- Exact runtime flags
- Context configuration
- Hardware limits

It’s comfortable.

---

## llama.cpp

llama.cpp is the engine.

No interface.
No abstraction.
Just direct control.

You run:

.\llama.exe -m models\model.gguf -p "Hello"

Now you are directly talking to the model.

No presets.
No hidden configurations.

If something behaves strangely,
you investigate.

That’s where understanding begins.

---

## Who is this for?

If you just want:
“AI on my PC”
Use LLM Studio.

If you want:
To understand what your hardware is doing,
To control memory usage,
To push limits,

You’ll end up in llama.cpp anyway.

And that’s where this site continues.
