""" ****************************************************
Aufgabe 7 Hauptdatei: GUI-Steuerung und Logik-Verbindung
*****************************************************"""

# Standard-Python-Module
import sys
import random

# PyQt5 und die generierte UI-Klasse
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import QTimer, Qt 
from ui_main_window import Ui_MainWindow


class Fangspiel(QMainWindow):
    # ANFORDERUNG: Maximal 10 Treffer
    MAX_TREFFER = 10 

    def __init__(self):
        super().__init__()
        
        # 1. UI-Setup: Die generierte Klasse initialisieren und Setup aufrufen
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # 2. Elemente zuweisen
        self.zeit_label = self.ui.zeit_label
        self.treffer_label = self.ui.treffer_label
        self.fang_button = self.ui.fang_button
        # Zugriff auf das Spielfeld-Widget (den Container des Buttons)
        self.spiel_bereich = self.ui.spiel_bereich 
        # SICHTBARKEIT: Stellt sicher, dass die Statuszeile ueber dem Spielfeld liegt
        self.ui.status_zeile.raise_() 
        
        # 3. Spielvariablen initialisieren
        self.spielzeit = 120
        self.treffer = 0
        self.spiel_aktiv = False
        
        # NEUE VARIABLEN FÜR DIE TESTERLEICHTERUNG
        self.bewegungs_intervall = 3 # <--- Button bewegt sich nur alle 3 Sekunden
        self.bewegungs_zaehler = 0   # Zaehlt die Sekunden bis zur naechsten Bewegung
        
        # 4. Layout-Override (Setzt den Button frei)
        # Trennt den Button vom Layout-Management, um freie Bewegung zu ermoeglichen.
        self.fang_button.setParent(self.spiel_bereich)
        self.fang_button.show()

        # 5. Timer einrichten und verbinden
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_spiel)
        self.fang_button.clicked.connect(self.button_geklickt)
        
        # 6. Spiel starten
        self.neues_spiel()

    # ------------------ SPIEL-LOGIK-METHODEN ------------------

    def neues_spiel(self):
        """Setzt das Spiel zurueck und startet den Timer."""
        self.spielzeit = 120
        self.treffer = 0
        self.spiel_aktiv = True
        self.bewegungs_zaehler = 0 # Zaehler zuruecksetzen
        self.fang_button.setText("Fang mich!")
        self.update_anzeige()
        self.timer.start(1000) 
        self.bewege_button()

    def update_anzeige(self):
        """Aktualisiert die Labels fuer Zeit und Treffer."""
        self.zeit_label.setText(f"Zeit: {self.spielzeit}")
        self.treffer_label.setText(f"Treffer: {self.treffer}")
        
        # ERZWINGEN DES NEUZEICHNENS zur Behebung  GUI-Probleme
        self.treffer_label.repaint() 

    def update_spiel(self):
        """Wird jede Sekunde vom Timer aufgerufen (Spielzeit-Logik)."""
        if self.spielzeit > 0:
            self.spielzeit -= 1
            self.update_anzeige()

            if self.spiel_aktiv and self.spielzeit == 0:
                self.spiel_beenden(gewonnen=False)
            
            elif self.spiel_aktiv:
                # NEUE BEWEGUNGS-LOGIK: Nur bewegen, wenn Intervall erreicht
                self.bewegungs_zaehler += 1
                if self.bewegungs_zaehler >= self.bewegungs_intervall:
                    self.bewege_button()
                    self.bewegungs_zaehler = 0 # Zaehler zuruecksetzen
                # Ende NEUE BEWEGUNGS-LOGIK

    def spiel_beenden(self, gewonnen: bool):
        """Beendet das Spiel und zeigt den Ergebnisdialog an."""
        self.timer.stop()
        self.spiel_aktiv = False
        
        # 1. Dialogtext festlegen
        if gewonnen:
            titel = "Spiel beendet"
            nachricht = "Herzlichen Glueckwunsch! Sie haben 10 Treffer erzielt." 
            icon = QMessageBox.Information
        else:
            titel = "Spiel beendet"
            nachricht = f"Sie haben leider verloren. Sie haben {self.treffer}/{self.MAX_TREFFER} Treffer erzielt."
            icon = QMessageBox.Warning
            
        # 2. QMessageBox erzeugen und anzeigen
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle(titel)
        msg_box.setText(nachricht)
        msg_box.setIcon(icon)
        
        # Schliesslogik
        msg_box.finished.connect(self.close)
        
        self.fang_button.setText("Spiel vorbei!")
        msg_box.exec_()
        
    def bewege_button(self):
        """Bewegt den Fang-Button an eine zufaellige Position INNERHALB des spiel_bereichs."""
        spielbereich_rect = self.spiel_bereich.rect()
        
        max_x = max(0, spielbereich_rect.width() - self.fang_button.width())
        max_y = max(0, spielbereich_rect.height() - self.fang_button.height())
        
        neue_x = random.randint(0, max_x)
        neue_y = random.randint(0, max_y)
        
        self.fang_button.move(neue_x, neue_y)
        
        # SICHTBARKEIT NEU ERZWINGEN
        self.ui.status_zeile.raise_()

    def button_geklickt(self):
        """Wird ausgeloest, wenn der Spieler den Button klickt."""
        if self.spiel_aktiv:
            self.treffer += 1
            self.update_anzeige()
            
            if self.treffer >= self.MAX_TREFFER:
                self.spiel_beenden(gewonnen=True)
            else:
                # Zaehler zuruecksetzen und sofort bewegen, wenn geklickt
                self.bewegungs_zaehler = 0 
                self.bewege_button()
        else:
            self.neues_spiel()


# Hauptanwendung starten
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling) 
    window = Fangspiel()
    window.show()
    sys.exit(app.exec_())