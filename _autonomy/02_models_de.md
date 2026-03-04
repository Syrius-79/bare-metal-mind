completion modelle vs chat modelle

(learning by doing)

Viele gehen davon aus, dass Completion-Modelle einfacher sind.

Das Gegenteil ist oft der Fall.

Ein Completion-Modell ist im Kern nur eine Textfortsetzungsmaschine.

Man gibt Tokens hinein.
Das Modell berechnet die nächsten Tokens.

Mehr passiert nicht.

Das Modell versteht keine Struktur wie:

Regeln

Rollen

Dialog

Systemanweisungen

Alles wird zu einer einzigen Tokenkette.

Beispiel:

identität
stil
regeln

nicci: ...
lola: ...

Für das Modell ist das keine Struktur.

Es ist nur Text.

Das Modell weiß nicht, was eine Regel ist.
Es weiß nicht, was Dialog bedeutet.

Es berechnet lediglich das wahrscheinlichste nächste Token.

Das führt zu einer wichtigen Erkenntnis:

die Struktur muss vom Entwickler gebaut werden.

pattern schlägt regel

Completion-Modelle folgen selten Regeln.

Sie folgen Mustern.

Ein kurzer Beispieldialog wie dieser:

nicci: hallo lola
lola: hallo nicci. was testest du heute?

nicci:

ist oft stärker als lange Regelblöcke.

Warum?

Weil das Modell jetzt sieht, wie ein Dialog aussieht.

LLMs kopieren Muster.

Sie gehorchen keinen Anweisungen.

chat / instruct modelle

Chat-Modelle werden anders trainiert.

Sie sehen immer wieder strukturierte Gespräche:

system: anweisung
user: frage
assistant: antwort

Dadurch entstehen interne Rollen.

Wenn das Modell

assistant:

sieht, weiß es automatisch, dass jetzt eine Antwort folgen soll.

Die Leitplanken sind bereits eingebaut.

der praktische unterschied

Completion-Modell

maximale Freiheit

maximale Instabilität

Struktur muss selbst gebaut werden

Chat-Modell

eingebaute Gesprächsstruktur

einfacher zu kontrollieren

weniger flexibel

beobachtung aus tests

Schon kleine Formulierungsänderungen können das Verhalten eines Completion-Modells komplett verändern.

Ein einzelnes Wort kann das Modell in eine andere Wahrscheinlichkeitsregion verschieben.

Beispiel:

hallo lola

gegenüber

hallo sklavin

Gleiches Modell.

Völlig andere Dynamik.

Das liegt nicht an „Intelligenz“.

Es ist reine Wahrscheinlichkeitsstatistik im Tokenraum.

fazit

Completion-Modelle sind rohe Werkzeuge.

Sie tun genau das, wofür sie gebaut wurden:

Text fortsetzen.

Wenn stabiles Verhalten gewünscht ist, muss die Umgebung sorgfältig gestaltet werden.

Prompting ist hier weniger ein Befehl.

Es ist eher das Aufbauen einer Bühne, auf der das Modell dann eine Rolle spielt.

Und manchmal entscheidet das Modell selbst, welches Stück gerade läuft.
