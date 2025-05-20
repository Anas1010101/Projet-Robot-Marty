# -*- coding: utf-8 -*-
"""
Created on Tue May 20 10:13:33 2025

@author: Dell
"""

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
from martypy import Marty

# Connexion au robot
IP_MARTY = "192.168.0.101"
try:
    marty = Marty("wifi", IP_MARTY)
except Exception as e:
    print(f"Erreur de connexion au robot : {e}")
    marty = None

class MartyControlPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contrôle du robot Marty")
        self.setGeometry(100, 100, 500, 300)

        self.layout = QVBoxLayout()

        self.create_direction_buttons()
        self.create_action_buttons()

        self.setLayout(self.layout)

    def create_direction_buttons(self):
        grid = QGridLayout()

        # Crée les boutons sans texte, mais avec des icônes
        btn_up = QPushButton()
        btn_down = QPushButton()
        btn_left = QPushButton()
        btn_right = QPushButton()

        # Définir les icônes (assure-toi que les fichiers existent à ces emplacements)
        btn_up.setIcon(QIcon("C:/Users/Dell/Desktop/Nouveau dossier/up.png"))
        btn_down.setIcon(QIcon("C:/Users/Dell/Desktop/Nouveau dossier/down.png"))
        btn_left.setIcon(QIcon("C:/Users/Dell/Desktop/Nouveau dossier/left.png"))
        btn_right.setIcon(QIcon("C:/Users/Dell/Desktop/Nouveau dossier/right.png"))

        # Ajuster la taille des icônes
        icon_size = QSize(48, 48)
        for btn in [btn_up, btn_down, btn_left, btn_right]:
            btn.setIconSize(icon_size)

        # Connecter les boutons aux actions du robot
        btn_up.clicked.connect(lambda: marty.walk(1))
        btn_down.clicked.connect(lambda: marty.walk(-1))
        btn_left.clicked.connect(lambda: marty.turn(-45))
        btn_right.clicked.connect(lambda: marty.turn(45))

        # Disposer les boutons dans une grille
        grid.addWidget(btn_up, 0, 1)
        grid.addWidget(btn_left, 1, 0)
        grid.addWidget(btn_right, 1, 2)
        grid.addWidget(btn_down, 2, 1)

        self.layout.addLayout(grid)

    def create_action_buttons(self):
        action_layout = QGridLayout()

        actions = {
            "Get Ready": lambda: marty.get_ready(),
            "Dance!": lambda: marty.dance(),
            "Wave Left": lambda: marty.wave("left"),
            "Wave Right": lambda: marty.wave("right"),
            "Kick Left": lambda: marty.kick("left"),
            "Kick Right": lambda: marty.kick("right"),
            "Wiggle Eyes": lambda: marty.eyes(1),
            "Show-off": lambda: marty.dance(steps=2)
        }

        # Disposition des boutons d’action en grille
        positions = [(i // 4, i % 4) for i in range(len(actions))]
        for (i, (label, function)) in zip(positions, actions.items()):
            btn = QPushButton(label)
            btn.clicked.connect(function)
            action_layout.addWidget(btn, i[0], i[1])

        self.layout.addLayout(action_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MartyControlPanel()
    window.show()
    sys.exit(app.exec())
