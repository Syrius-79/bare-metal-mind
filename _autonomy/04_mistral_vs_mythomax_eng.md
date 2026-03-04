---
layout: guide
title: Mistral vs MythoMax – Stability Observation
order: 4
---

# Mistral vs MythoMax – Stability Observation

This note documents a simple real-world observation when running local LLMs with llama.cpp.

No synthetic benchmarks.  
No leaderboard comparisons.

Just continuous generation under identical runtime parameters.

---

# Models

Mistral


mistral-7b-instruct-v0.1.Q4_K_M.gguf


MythoMax


MythoMax-L2-13b.Q4_K_M.gguf


Both models were executed using the same llama.cpp configuration.

Example server configuration:


llama-server
--model MODEL.gguf
--ctx-size 2048
--threads 8
--batch-size 2048
--parallel 1
--cache-ram 0


---

# Observation

During long continuous generation the following behavior appeared.

### Mistral 7B

After approximately **4–5 minutes of continuous generation**, the model began drifting.

Typical symptoms included:

- repetition loops
- semantic instability
- degraded continuation quality

The model effectively "collapsed" into unstable output.

### MythoMax 13B

Under the same configuration MythoMax continued generating for **30+ minutes without collapse**.

Output remained coherent and stable.

No repetition loops appeared during the observation period.

---

# Possible explanation

This difference is likely related to training and alignment characteristics rather than parameter count alone.

Many Mistral instruct variants are strongly optimized for:

- short instruction responses
- chat interactions
- fast completion cycles

MythoMax, built on LLaMA-2, was fine-tuned for:

- roleplay
- narrative continuation
- longer text generation

These training choices may produce more stable token distributions during long sequences.

---

# Context configuration

Training context:


4096 tokens


Runtime configuration:


--ctx-size 2048


Operating below the trained context window can reduce attention noise and sometimes improves stability.

---

# Conclusion

Under identical runtime conditions:

**MythoMax demonstrated significantly higher stability during long continuous generation than Mistral.**

This is a practical observation based on real usage, not a formal benchmark.

Further structured testing may be added later.
