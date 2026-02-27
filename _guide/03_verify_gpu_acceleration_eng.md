---
layout: guide
title: How to Verify GPU Acceleration (CPU vs GPU Explained Properly)
order: 3
---

# How to Verify GPU Acceleration — CPU vs GPU, No Illusions

You think you're using your GPU.

Are you?

Let’s break something simple that many people never truly understand:

CPU and GPU are not the same thing.
They are built for different kinds of work.

---

## CPU vs GPU — What Actually Changes?

CPU:

- Few cores
- Very strong per-core performance
- Designed for general tasks
- Handles operating system logic
- Good at sequential operations

GPU:

- Thousands of smaller cores
- Designed for parallel math
- Built for matrix multiplication
- Perfect for neural networks

An LLM is mostly matrix multiplication.

That’s GPU territory.

If your CPU is doing it,
it will work —
but it will crawl.

---

## What Happens Without GPU Acceleration?

If llama.cpp runs on CPU only:

- All tensor operations run on main RAM
- Your CPU usage spikes
- Fans spin
- Tokens per second are low
- Larger models feel painful

It works.
But it feels heavy.

That’s not acceleration.
That’s endurance.

---

## What Happens With GPU Acceleration?

When CUDA is active and layers are offloaded:

- VRAM usage increases
- GPU utilization rises
- CPU load drops
- Tokens per second increase significantly
- Generation feels fluid

Now you're using silicon designed for this job.

This is not subtle.
The difference is obvious.

---

## The Common Illusion

Many users do this:

They install drivers.
They compile llama.cpp.
They run a model.
It generates text.

They assume:
"GPU is working."

No.

The model running does not mean the GPU is active.

Acceleration must be observable.

---

## How To Check Properly (NVIDIA)

Open a terminal.

nvidia-smi

Keep it open.

Start text generation.

Watch:

- Memory (VRAM)
- GPU Utilization %

If VRAM increases while generating,
and utilization spikes,
your GPU is active.

If it stays near zero,
you are on CPU.

No theory.
No guessing.

Just numbers.

---

## Advanced Reality Check

If you're serious:

Compare tokens per second.

CPU-only:
Low.
Stable.
Hot.

GPU-accelerated:
Higher.
Smoother.
Noticeably faster.

If you can't tell the difference,
you are not pushing the system hard enough.

---

## Why This Matters

Acceleration is not about ego.

It determines:

- Which models you can realistically run
- How large context can grow
- Whether experimentation feels painful or fluid
- Whether this is a toy — or a tool

CPU-only is valid.

But GPU acceleration is a different league.

If you're reading this,
you probably care which league you're in.

Next:
Why “uncensored” models sometimes refuse — and why it’s not random.
Run:

