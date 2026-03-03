# Controlled Autonomy – Phase I
## From Model to System

The model is probabilistic.  
The system is deterministic.  

The difference is everything.

---

## 1. Core Agent Loop (v0.1)

1. Receive input  
2. Generate structured decision  
3. Validate decision  
4. Execute whitelisted tool  
5. Log result  
6. Reflect on outcome  

No hidden magic.  
No romantic AI mythology.

---

## 2. Why Both (Plan + Reflection)?

Because models hallucinate confidence.

Reflection reduces drift.  
Logging exposes instability.  
Structure limits damage.

An unstructured agent becomes roleplay.  
A structured agent becomes a system.

---

## 3. Minimal Execution Model

### Brain
- `llama-server`

### Controller
- `agent_core.py`

### Tool Layer
- Explicit whitelist
- No shell execution by default

### Memory
- Structured JSON nodes
- Append-only logs

---

## 4. Design Constraints

- The model is not trusted.
- Every tool call is validated.
- All actions are logged.
- No blind file writes.
- No uncontrolled system access.

---

## 5. Failure Philosophy

Failure is not hidden.

If the agent:
- selects the wrong tool  
- misinterprets a goal  
- loops incorrectly  
- shows overconfidence  

It is documented.

This repository does not perform.  
It measures.

---

## MA PLAUNSCH.

Improvisation is allowed.  
Control is mandatory.


---

# Kontrollierte Autonomie – Phase I (Kurzfassung)

Ein Modell ist probabilistisch.  
Ein System ist deterministisch.  

Der Unterschied ist entscheidend.

## Kernidee

Wir bauen keinen Chatbot.  
Wir bauen eine kontrollierte Ausführungsarchitektur.

Das System:

1. Empfängt Eingabe  
2. Trifft eine strukturierte Entscheidung  
3. Validiert diese Entscheidung  
4. Führt nur freigegebene Tools aus  
5. Protokolliert alles  
6. Bewertet das Ergebnis  

## Warum Planung + Reflexion?

Modelle simulieren Sicherheit.

Reflexion reduziert Drift.  
Logging macht Instabilität sichtbar.  
Struktur begrenzt Schaden.

Ein unstrukturiertes Modell wird Rollenspiel.  
Ein strukturiertes Modell wird System.

## Prinzip

- Das Modell wird nicht blind vertraut.
- Tool-Zugriff ist strikt begrenzt.
- Jede Aktion wird dokumentiert.
- Fehler werden nicht versteckt.

Hier wird nicht inszeniert.  
Hier wird geprüft.

---

MA PLAUNSCH.
Improvisation ist erlaubt. Kontrolle ist Pflicht.



