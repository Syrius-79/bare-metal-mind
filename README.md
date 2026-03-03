# BARE METAL MIND

Most people don’t run powerful LLMs.

They run unstable ones.

They increase temperature.  
They copy prompts.  
They blame the model.

Then they say:  
“LLMs are overrated.”

No.

They were never under control.

---

## MODEL BASELINE

Unless explicitly stated otherwise,  
all experiments in this repository are based on:

- Base completion models (v1-style)
- No enforced chat template
- No system / user / assistant role dependency
- Raw token continuation behavior

**Example baseline:**  
Mythomax (GGUF)

This repository starts from the simplest possible model behavior.

No chat abstraction layer.  
No role formatting assumptions.  
No hidden scaffolding.

If a document relies on structured chat roles  
(system / user / assistant),  
it will be explicitly marked.

No silent architectural shifts.

---

## WHAT THIS REPOSITORY IS

This repository documents structured testing of local Large Language Models.

### Focus Areas

- Constraint  
- Drift  
- Behavioral Stability  
- Context Pressure  
- Parameter Control  

Tested on real hardware.  
Under real limits.  
Without API abstraction layers.

No hype.  
No prompt magic.  
No AI influencer theatre.

Only systems under load.

---

## WHY START WITH V1-STYLE MODELS?

Base completion models are the smallest controllable unit.

They:

- Do not inject role priors  
- Do not assume conversational formatting  
- Do not override orchestration structure  

They simply continue tokens.

Controlling this behavior is already difficult.

Before adding role-based chat structure,
the base behavior must be understood and stabilized.

Role-based / assistant-structured models  
introduce additional behavioral layers.

Those will be documented separately  
and clearly labeled when addressed.

---

## SWISS ENGINEERING CONTEXT (CH)

Built from a Swiss systems mindset.

Precision.  
Discipline.  
Constraint.  
Accountability.

Systems must behave predictably.  
If they do not, the fault is structural.

Large Language Models are stochastic engines operating under constraint.

Temperature = Pressure  
Context Length = Structural Load  
Sampling = Bias Control  

Drift is not mystical.  
Drift is mechanical instability.

---

## LANGUAGE & TEST SCOPE

Primary documentation language: English.

Core experiments conducted in:

- English  
- Standard German (CH/D context)

Additional validation tests executed in Swiss German dialect.

Language is not decoration.  
It is a control variable.

Different linguistic environments influence:

- Token distribution  
- Instruction compliance  
- Verbosity  
- Alignment smoothing  
- Drift behavior  

Translation preserves wording.  
It does not preserve behavioral stress.

---

## SYSTEMREALITÄT (D/CH)

Dieses Repository dokumentiert strukturierte Tests mit lokalen LLMs.

Keine Spielerei.  
Keine Marketing-Sprache.

Ein LLM ist ein Wahrscheinlichkeitsmodell unter Last.

Ohne Struktur entsteht Durchschnitt.  
Ohne Begrenzung entsteht Drift.  
Unter Druck zeigt sich Systemverhalten.

Hier wird nicht inszeniert.  
Hier wird geprüft.

---

# MA PLAUNSCH.
