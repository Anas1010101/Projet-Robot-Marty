# -*- coding: utf-8 -*-
"""
Created on Fri May 23 01:12:57 2025

@author: Dell
"""

from martypy import Marty

# Connexion au robot
IP_MARTY = "192.168.0.101"  # à adapter selon votre configuration réseau
try:
    marty = Marty("wifi", IP_MARTY)
except Exception as e:
    print(f"Erreur de connexion : {e}")
    marty = None

def detecter_et_agir():
    if marty:
        try:
            couleur = marty.get_colour()
            print(f"Couleur détectée : {couleur}")

            # Actions selon la couleur détectée
            if couleur == "red":
                marty.dance()
            elif couleur == "blue":
                marty.wave("left")
            elif couleur == "green":
                marty.kick("right")
            elif couleur == "yellow":
                marty.turn(90)
            else:
                print("Aucune action définie pour cette couleur.")

        except Exception as e:
            print(f"Erreur lors de la détection : {e}")
    else:
        print("Robot non connecté.")

# Test de la fonction
if __name__ == "__main__":
    detecter_et_agir()
