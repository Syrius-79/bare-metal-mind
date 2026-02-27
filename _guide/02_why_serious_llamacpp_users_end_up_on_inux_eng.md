---
layout: post
title: "Why Linux Wins for llama.cpp (And How To Install It Properly)"
---

# Why Linux Wins for llama.cpp

You got it running on Windows.

Good.

Now you want it done properly.

This is where Linux wins.

Not because it’s cool.

Because it’s transparent.

---

## Important before you continue

Paths change.  
Package names change.  
Binary names change.  
Distros behave differently.

This is not a step-by-step babysitting guide.

You are expected to read.

You are expected to check versions.

Always download from official sources.
Never random mirrors.

---

## What you actually need

You need:

- A Linux distribution (Ubuntu is fine, others work too)
- A working GPU (if you want acceleration)
- Correct drivers
- The current version of llama.cpp

That’s it.

No magic.

---

## Where to download

Linux distro  
→ ubuntu.com  

NVIDIA drivers & CUDA (if you have an NVIDIA GPU)  
→ nvidia.com  

llama.cpp  
→ github.com/ggerganov/llama.cpp  

Models (GGUF format)  
→ huggingface.co  

Always download the latest stable versions from the official websites.

Do not rely on outdated blog commands.
Do not trust random YouTube tutorials.

Things change fast.

---

## About GPUs

Not everyone has an NVIDIA GPU.

If you have NVIDIA:
Use official drivers.
Verify with:

nvidia-smi

If that command shows your GPU,
your driver is active.

If it doesn’t:
Fix that first.

If you don’t have NVIDIA:
llama.cpp still runs.
Just slower.
CPU-only is valid.
It’s just less dramatic.

---

## Why Linux feels different

On Windows, you run a binary.

On Linux, you build the engine.

You see dependencies.
You see compile flags.
You see what links against what.

You’re not guessing.

You’re watching.

That changes how you think about local AI.

---

## Final reality check

If you want convenience,
Windows is fine.

If you want performance,
stability,
and real control,

Linux wins.

Every time.

---

Next:
How to verify your system is actually using acceleration — and not pretending.
