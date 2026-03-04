# Sampling Is Not Intelligence

Many users assume that a language model “thinks”.

It does not.

A model only predicts the next token.

The behaviour of the system is largely controlled by the sampling configuration.

## Token Selection

During generation the model calculates probabilities for every possible next token.

The sampler then selects one token according to its configuration.

Common parameters include:

- temperature
- top_p
- top_k
- repetition_penalty

These parameters influence how predictable or chaotic the output becomes.

## Determinism vs Exploration

Low temperature leads to deterministic outputs.

The model repeatedly chooses the most probable tokens.

This creates stable but often repetitive text.

Higher temperature allows exploration of less probable tokens.

This can produce more diverse outputs, but also instability.

## Why Models Sometimes Look “Dumb”

When sampling parameters are poorly configured, the output may appear incoherent.

This is not a failure of the model.

It is simply the result of the probability distribution being sampled differently.

The model is always doing the same thing:

predicting the next token.

## Reality

A language model does not reason.

It samples from probabilities.
