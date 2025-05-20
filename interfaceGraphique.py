# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from martypy import Marty

# Adresse IP de ton robot (à remplacer par la tienne)
IP_MARTY = "192.168.0.102"
marty = Marty("wifi", IP_MARTY)

class MartyControlWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Contrôle de Marty le robot")
        self.setGeometry(100, 100, 300, 200)

        # Création des boutons
        btn_marche = QPushButton("Marcher")
        btn_danse = QPushButton("Danser")
        btn_tourne = QPushButton("Tourner")

        # Connexion des boutons aux fonctions
        btn_marche.clicked.connect(self.marche)
        btn_danse.clicked.connect(self.danse)
        btn_tourne.clicked.connect(self.tourne)

        # Disposition verticale
        layout = QVBoxLayout()
        layout.addWidget(btn_marche)
        layout.addWidget(btn_danse)
        layout.addWidget(btn_tourne)

        self.setLayout(layout)

    def marche(self):
        marty.walk(10)

    def danse(self):
        marty.dance()

    def tourne(self):
        marty.turn(90)

# Lancement de l'application
app = QApplication(sys.argv)
window = MartyControlWindow()
window.show()
sys.exit(app.exec())
