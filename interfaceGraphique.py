import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QGridLayout, QProgressBar
)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import QTimer, Qt, QSize

# Définition de la fenêtre principale de l'application
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.setWindowTitle("Interface Robot Marty")   # Titre de la fenêtre
        self.setFixedSize(800, 400)                    # Taille fixe (largeur=800, hauteur=400)
        self.setStyleSheet("background-color: #D3D3D3;")  # Couleur de fond gris clair

        # Bouton pour déconnecter le robot
        self.disconnect_button = QPushButton("Déconnecter")

        # Étiquette pour afficher l'état de la batterie
        self.battery_label = QLabel()
        # Barre de progression pour le niveau de batterie (de 0 à 100)
        self.battery_progress = QProgressBar()
        self.battery_progress.setRange(0, 100)
        self.battery_progress.setTextVisible(False)  # Ne pas afficher le texte dans la barre

        # Étiquette pour afficher la couleur détectée par le capteur
        self.sensor_color_label = QLabel()
        # Carré coloré (30x30 pixels) pour montrer visuellement la couleur détectée
        self.sensor_color_square = QLabel()
        self.sensor_color_square.setFixedSize(30, 30)

        # Boutons de contrôle pour déplacer le robot Marty
        self.btn_forward = QPushButton("\u2191")  # Flèche haut (avancer)
        self.btn_backward = QPushButton("\u2193") # Flèche bas (reculer)
        self.btn_left = QPushButton("\u2190")     # Flèche gauche (aller à gauche)
        self.btn_right = QPushButton("\u2192")    # Flèche droite (aller à droite)
        self.btn_turn_left = QPushButton("\u2196") # Flèche diagonale haut-gauche (tourner à gauche)
        self.btn_turn_right = QPushButton("\u2197")# Flèche diagonale haut-droite (tourner à droite)

        # Boutons d'actions supplémentaires pour le robot
        self.btn_eyes = QPushButton("Set Eyes")             # Changer l'expression des yeux
        self.btn_dance = QPushButton("Start Dancing")       # Lancer une danse
        self.btn_celebrate = QPushButton("Start Celebrating") # Lancer une célébration
        self.btn_close = QPushButton("Close")                # Fermer l'application

        # Mise en forme des boutons de contrôle (taille, police, couleurs)
        control_buttons = [
            self.btn_forward, self.btn_backward, self.btn_left, self.btn_right,
            self.btn_turn_left, self.btn_turn_right
        ]
        for btn in control_buttons:
            btn.setFixedSize(QSize(70, 70))  # Taille carrée de 70x70 pixels
            btn.setFont(QFont("Arial", 20))  # Police Arial, taille 20
            btn.setStyleSheet("background-color: black; color: white; border-radius: 5px;")  # Style noir avec texte blanc et bords arrondis

        # Mise en forme des boutons d'action (taille, couleur, police)
        action_buttons = [self.btn_eyes, self.btn_dance, self.btn_celebrate, self.btn_close]
        for btn in action_buttons:
            btn.setFixedSize(QSize(150, 40))  # Taille plus large que les boutons de contrôle
            btn.setStyleSheet("background-color: #269993; color: white; font-size: 16px; border-radius: 5px;")  # Fond vert/bleu, texte blanc, bords arrondis

        # Style spécifique pour le bouton de déconnexion (rouge vif)
        self.disconnect_button.setStyleSheet("background-color: #dc3545; color: white; font-weight: bold;")

        # Organisation des boutons de contrôle dans une grille 3x3 simplifiée
        grid_layout = QGridLayout()
        grid_layout.addWidget(self.btn_turn_left, 0, 0)  # Coin haut-gauche
        grid_layout.addWidget(self.btn_forward, 0, 1)    # Centre haut
        grid_layout.addWidget(self.btn_turn_right, 0, 2) # Coin haut-droit
        grid_layout.addWidget(self.btn_left, 1, 0)       # Milieu gauche
        grid_layout.addWidget(self.btn_right, 1, 2)      # Milieu droite
        grid_layout.addWidget(self.btn_backward, 2, 1)   # Centre bas

        # Disposition verticale des boutons d'action
        action_layout = QVBoxLayout()
        for btn in action_buttons:
            action_layout.addWidget(btn)

        # Layout pour les infos : bouton déconnexion, batterie, couleur détectée
        info_layout = QVBoxLayout()

        # Disposition horizontale pour la batterie (label + barre)
        battery_layout = QHBoxLayout()
        battery_layout.addWidget(self.battery_label)
        battery_layout.addWidget(self.battery_progress)

        # Disposition horizontale pour la couleur (label + carré coloré)
        color_layout = QHBoxLayout()
        color_layout.addWidget(self.sensor_color_label)
        color_layout.addWidget(self.sensor_color_square)

        # Ajout des éléments dans la colonne info
        info_layout.addWidget(self.disconnect_button)
        info_layout.addLayout(battery_layout)
        info_layout.addLayout(color_layout)

        # Layout principal horizontal : boutons contrôle + espace + actions + espace + infos
        main_layout = QHBoxLayout()
        main_layout.addLayout(grid_layout)
        main_layout.addSpacing(50)   # Espace horizontal entre sections
        main_layout.addLayout(action_layout)
        main_layout.addSpacing(50)
        main_layout.addLayout(info_layout)

        # Création d'un widget central pour contenir tout le layout
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)  # Définir le widget central de la fenêtre

# Point d'entrée du programme
if __name__ == "__main__":
    app = QApplication(sys.argv)  # Création de l'application PyQt
    window = MainWindow()         # Création de la fenêtre principale
    window.show()                # Affichage de la fenêtre
    sys.exit(app.exec())         # Lancement de la boucle d'événements
