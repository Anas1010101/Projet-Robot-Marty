# Importation de la bibliothèque martypy (interface avec le robot Marty)
from martypy import Marty

# Connexion au robot Marty en Wi-Fi avec son adresse IP
my_marty = Marty("wifi", "192.168.0.111")

# --- Fonctions de déplacement ---

def move_on():
    """
    Fait marcher Marty vers l'avant.
    - 7 pas
    - pied de départ automatique
    - pas de rotation (turn=0)
    - longueur de pas : 25 mm
    - durée totale du mouvement : 1000 ms
    """
    my_marty.walk(num_steps=7, start_foot='auto', turn=0, step_length=25, move_time=1000)
    my_marty.stand_straight()  # Se remet droit après avoir marché


def move_back():
    """
    Fait marcher Marty vers l'arrière.
    Identique à move_on, mais avec une longueur de pas négative.
    """
    my_marty.walk(num_steps=7, start_foot='auto', turn=0, step_length=-25, move_time=1000)
    my_marty.stand_straight()


def step_right():
    """
    Fait faire à Marty 7 pas de côté vers la droite.
    """
    my_marty.sidestep("right", 7)
    my_marty.stand_straight()


def step_left():
    """
    Fait faire à Marty 7 pas de côté vers la gauche.
    """
    my_marty.sidestep("left", 7)
    my_marty.stand_straight()


def turn_left():
    """
    Fait tourner Marty vers la gauche.
    Valeur de rotation : +15 degrés environ.
    """
    my_marty.walk(turn=15, move_time=1000)


def turn_right():
    """
    Fait tourner Marty vers la droite.
    Valeur de rotation : -15 degrés environ.
    """
    my_marty.walk(turn=-15, move_time=1000)
