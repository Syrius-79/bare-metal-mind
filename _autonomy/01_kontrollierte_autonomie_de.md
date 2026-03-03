# Kontrollierte Autonomie – Phase I
## Vom Modell zum System

Ein Modell erzeugt Token.  
Ein System erzwingt Struktur.

Ein Modell ist probabilistisch.  
Ein System ist deterministisch.

Der Unterschied ist entscheidend.

---

## 1. Kern-Schleife (v0.1)

1. Eingabe empfangen  
2. Strukturierte Entscheidung erzeugen  
3. Entscheidung validieren  
4. Freigegebenes Tool ausführen  
5. Ergebnis protokollieren  
6. Ergebnis reflektieren  

Keine versteckte Magie.  
Keine romantische KI-Mythologie.

---

## 2. Warum Planung + Reflexion?

Modelle simulieren Sicherheit.

Sie können überzeugend klingen und dennoch falsch liegen.

Reflexion reduziert Drift.  
Logging macht Instabilität sichtbar.  
Struktur begrenzt Schaden.

Ein unstrukturiertes Modell wird Rollenspiel.  
Ein strukturiertes Modell wird System.

---

## 3. Minimales Ausführungsmodell

### Gehirn
- `llama-server`

### Controller
- `agent_core.py`

### Tool-Ebene
- Explizite Whitelist
- Kein direkter Shell-Zugriff
- Keine unkontrollierten Dateizugriffe

### Speicher
- Strukturierte JSON-Knoten
- Append-only Logs

---

## 4. Prinzipien

- Dem Modell wird nicht blind vertraut.
- Tool-Zugriff ist strikt begrenzt.
- Jede Aktion wird dokumentiert.
- Fehler werden nicht versteckt.
- Drift wird erwartet und gemessen.

Hier wird nicht inszeniert.  
Hier wird Systemverhalten geprüft.

---

MA PLAUNSCH.
Improvisation ist erlaubt. Kontrolle ist Pflicht.
