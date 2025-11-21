# Fangspiel (GUI Desktop Anwendung)

Ein interaktives Reaktionsspiel, entwickelt mit Python und dem Qt-Framework. Ziel der Anwendung ist es, eine sich zufällig bewegende Schaltfläche innerhalb eines definierten Zeitlimits mit der Maus zu klicken.

## Aufgabenstellung
Entwicklung einer grafischen Anwendung mit folgenden Anforderungen:
1.  Erstellung eines Formulars mit einer Schaltfläche, die gefangen werden muss.
2.  Dynamische Positionierung: Die Schaltfläche soll ihre Position im Formular regelmäßig und zufällig wechseln.
3.  Begrenzung: Die neue Position muss so berechnet werden, dass die Schaltfläche immer vollständig innerhalb des Formulars sichtbar bleibt.
4.  Zeitsteuerung: Die Schaltfläche muss lange genug an einer Position verweilen (mindestens 1 Sekunde), um anklickbar zu sein.
5.  Spielablauf: Das Spiel endet nach maximal zwei Minuten oder wenn das Ziel erreicht wurde.

## Technische Umsetzung
Der Quellcode demonstriert fortgeschrittene Techniken der GUI-Programmierung:

- Timer-Steuerung (QTimer): Verwendung eines Timers zur Steuerung der Spielzeit (Countdown) und eines Intervalls für die Bewegung des Buttons.
- Absolute Positionierung: Der Button wird aus dem Standard-Layout gelöst, um mittels Koordinaten (.move) frei auf dem Spielfeld platziert zu werden.
- Kollisionsvermeidung: Berechnung der maximalen X- und Y-Koordinaten basierend auf der Fenstergröße abzüglich der Button-Größe, um ein Verschwinden aus dem Sichtbereich zu verhindern.
- UI-Integration: Trennung von Design (ui-Datei) und Programmlogik.

## Dateistruktur
Das Projekt besteht aus drei zentralen Dateien:
- fangspiel.py: Die Hauptdatei mit der Spiellogik (Timer, Bewegung, Klick-Events).
- main_window_ui.ui: Die Design-Datei (erstellt mit Qt Designer).
- ui_main_window.py: Die von Qt kompilierte Python-Datei der Oberfläche.

## Installation und Start
Voraussetzung ist eine installierte Python-Umgebung sowie die PyQt5-Bibliothek.

Installation der Bibliothek:
pip install PyQt5

Start der Anwendung:
python fangspiel.py
