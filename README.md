# Fangspiel (GUI Desktop Anwendung)

Ein interaktives Reaktionsspiel, entwickelt mit Python und dem Qt-Framework. Ziel der Anwendung ist es, eine sich zufällig bewegende Schaltfläche innerhalb eines definierten Zeitlimits mit der Maus zu klicken.

## Aufgabenstellung
Entwicklung einer grafischen Anwendung mit folgenden Anforderungen:
1.  Erstellung eines Formulars mit einer Schaltfläche, die gefangen werden muss.
2.  Dynamische Positionierung: Die Schaltfläche soll ihre Position im Formular regelmäßig und zufällig wechseln, dabei aber immer vollständig sichtbar bleiben.
3.  Zeitsteuerung: Die Schaltfläche muss mindestens eine Sekunde lang an einer Position verweilen, um anklickbar zu sein.
4.  Statusanzeige: Am unteren Rand des Formulars müssen die aktuelle Trefferzahl und die verbleibende Spielzeit (in Sekunden) eingeblendet werden.
5.  Spielende: Das Spiel endet nach maximal zwei Minuten oder sobald 10 Treffer erzielt wurden.
6.  Dialoge:
    - Bei 10 Treffern: Anzeige einer Erfolgsmeldung ("Herzlichen Glückwunsch").
    - Bei Zeitablauf ohne 10 Treffer: Anzeige einer Niederlage-Meldung.
    - Die Umsetzung der Dialoge muss zwingend über die Klasse QMessageBox erfolgen.
7.  Programmfluss: Nach Schließen des Dialogs muss das gesamte Programm beendet werden.

## Technische Umsetzung
Der Quellcode demonstriert fortgeschrittene Techniken der GUI-Programmierung mit PyQt5:

- Timer-Steuerung (QTimer): Verwendung eines Timers zur Steuerung des Countdowns und des Bewegungsintervalls.
- Absolute Positionierung: Der Button wird aus dem Layout gelöst (.setParent), um mittels Koordinatenberechnung frei platziert zu werden.
- Kollisionsberechnung: Algorithmus zur Sicherstellung, dass der Button nicht über die Fenstergrenzen hinausragt.
- Dialog-Management: Implementierung von QMessageBox für Feedback (Information/Warning) und Nutzung des 'finished'-Signals zum sauberen Beenden der Anwendung.
- UI-Integration: Trennung von Design (ui-Datei) und Programmlogik.

## Dateistruktur
Das Projekt besteht aus drei zentralen Dateien:
- fangspiel.py: Die Hauptdatei mit der kompletten Spiellogik.
- main_window_ui.ui: Die Design-Datei (erstellt mit Qt Designer).
- ui_main_window.py: Die von Qt kompilierte Python-Datei der Oberfläche.

## Installation und Start
Voraussetzung ist eine installierte Python-Umgebung sowie die PyQt5-Bibliothek.

Installation der Bibliothek:
pip install PyQt5

Start der Anwendung:
python fangspiel.py
