# Controlled Autonomy – Phase I
## From Model to System

A model predicts tokens.  
A system enforces structure.

A model is probabilistic.  
A system is deterministic.

The difference is everything.

---

## 1. Core Loop (v0.1)

1. Receive input  
2. Generate structured decision  
3. Validate decision  
4. Execute whitelisted tool  
5. Log result  
6. Reflect on outcome  

No hidden magic.  
No romantic AI mythology.

---

## 2. Why Planning + Reflection?

Models simulate confidence.

They can sound certain while being wrong.

Reflection reduces drift.  
Logging exposes instability.  
Structure limits damage.

An unstructured model becomes roleplay.  
A structured model becomes a system.

---

## 3. Minimal Execution Model

### Brain
- `llama-server`

### Controller
- `agent_core.py`

### Tool Layer
- Explicit whitelist
- No blind shell execution
- No uncontrolled file writes

### Memory
- Structured JSON nodes
- Append-only logs

---

## 4. Principles

- The model is not trusted blindly.
- Tool access is strictly limited.
- Every action is logged.
- Failure is documented.
- Drift is expected and measured.

This repository does not perform.  
It measures behavior under constraint.

---

MA PLAUNSCH.
Improvisation is allowed. Control is mandatory.
