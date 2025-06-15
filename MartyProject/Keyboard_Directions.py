# Importation des modules nécessaires
import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

# Importation des fonctions de contrôle (déplacement de Marty)
from Marty_Detection import move_on     # avance (Z)
from Marty_Detection import move_back   # recule (S)
from Marty_Detection import step_right  # droite (Q)
from Marty_Detection import step_left   # gauche (D)

# Création de la fenêtre principale
class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Titre de la fenêtre
        self.setWindowTitle("Test des touches")

        # Dimensions initiales de la fenêtre
        self.resize(400, 100)

        # Permet de capter les événements clavier
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

    def keyPressEvent(self, event):
        """
        Gère les touches clavier appuyées.
        Associe les touches Z, S, Q, D à des fonctions importées.
        """
        if event.key() == Qt.Key.Key_Z:
            move_on()       # Avancer
        elif event.key() == Qt.Key.Key_S:
            move_back()     # Reculer
        elif event.key() == Qt.Key.Key_Q:
            step_right()    # Pas à droite
        elif event.key() == Qt.Key.Key_D:
            step_left()     # Pas à gauche

# Point d'entrée de l’application
if __name__ == "__main__":
    app = QApplication(sys.argv)   # Création de l'application PyQt
    window = MyWindow()            # Instanciation de la fenêtre personnalisée
    window.show()                  # Affichage de la fenêtre
    sys.exit(app.exec())           # Boucle principale (évite que le programme se ferme)
