---
layout: guide
title: Token Drift During Long Generation
order: 5
---

# Token Drift During Long Generation

When running local LLMs for extended generation, a common phenomenon appears:

**token drift**

This describes the gradual loss of semantic stability in long outputs.

Instead of continuing coherently, the model begins to:

- repeat phrases
- lose topic consistency
- generate unstable or meaningless text

This effect is not a bug in the software.  
It is a natural property of probabilistic language models.

---

# Why Token Drift Happens

Large language models generate text one token at a time.

Each new token is sampled from a probability distribution based on the previous context.

Over time small probability deviations accumulate.

A simplified view:

1. token A is slightly off
2. token B is sampled based on A
3. token C is sampled based on A+B
4. the error compounds

After many generations the model may drift away from the original semantic path.

This is similar to numerical error accumulation in long iterative calculations.

---

# Typical Symptoms

During long generation sessions token drift often appears as:

Repetition loops

Example:


the system will continue to continue to continue to continue


Topic decay

The model slowly forgets the original context.

Instruction collapse

The model stops following instructions and generates unrelated text.

---

# Factors That Influence Drift

Several parameters affect how quickly drift appears.

Temperature

Higher temperature increases randomness and accelerates drift.

Context window

Very long contexts can introduce attention noise.

Model training

Models trained for long narrative tasks often drift slower than models tuned for short chat responses.

---

# Practical Observation

In practical tests different models show different stability characteristics.

Some instruction-tuned models collapse after only a few minutes of continuous generation.

Narrative-oriented models often maintain coherence much longer.

This suggests that **training objectives strongly influence long-sequence stability.**

---

# Conclusion

Token drift is a natural property of autoregressive language models.

It becomes visible when:

- generation runs for long periods
- sampling randomness accumulates
- context becomes unstable

Understanding this behavior is important when evaluating local models.

Benchmarks rarely show it.

Real usage does.
