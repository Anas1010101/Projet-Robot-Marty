# Importe la fonction sleep pour faire des pauses dans le programme
from time import sleep 

# Importe la bibliothèque martypy pour contrôler le robot Marty
from martypy import Marty

# Fonction pour convertir une couleur hexadécimale (ex: "FF0000") en valeurs RGB
def hex_to_rgb(hex_color):
    red = int(hex_color[0:2], 16)    # Extrait et convertit les 2 premiers caractères en rouge (base 16 → base 10)
    green = int(hex_color[2:4], 16)  # Extrait et convertit les 2 suivants pour le vert
    blue = int(hex_color[4:6], 16)   # Extrait et convertit les 2 derniers pour le bleu
    return red, green, blue

# Fonction qui vérifie si une valeur est dans une plage de tolérance autour d’une valeur cible
def within_tolerance(value, target, tolerance):
    return abs(value - target) <= tolerance

# Fonction qui compare une couleur RGB donnée à une liste de couleurs de référence
# et retourne le nom de la couleur correspondante
def detect_color(r, g, b, color_ranges):
    for color, values in color_ranges.items():
        if (within_tolerance(r, values["r"], values["tolerance"]) and
                within_tolerance(g, values["g"], values["tolerance"]) and
                within_tolerance(b, values["b"], values["tolerance"])):
            return color  # Couleur reconnue
    return "unknown"     # Aucune couleur ne correspond

# Connexion au robot Marty via Wi-Fi avec son adresse IP
marty = Marty("wifi", "192.168.0.103")

# On désactive le mode "blocking", ce qui signifie que Marty peut continuer d’exécuter des commandes en parallèle
marty.set_blocking(False)

# Le robot se met debout en position neutre
marty.stand_straight()

# Boucle principale qui tourne indéfiniment
while True:
    sleep(2)  # Attente de 2 secondes entre chaque lecture du capteur

    # Récupération de la couleur détectée par le capteur gauche de Marty
    hex_color = str(marty.get_color_sensor_hex("LeftColorSensor"))

    # Conversion de la couleur hexadécimale en valeurs RGB
    red_value, green_value, blue_value = hex_to_rgb(hex_color)
    print(f"Red: {red_value} | Green: {green_value} | Blue: {blue_value}")

    # Définition des couleurs de référence avec une tolérance sur chaque composante
    color_ranges = {
        "red": {"r": 126, "g": 23, "b": 33, "tolerance": 13},
        "green": {"r": 46, "g": 43, "b": 40, "tolerance": 13},
        "yellow": {"r": 17, "g": 103, "b": 5, "tolerance": 13},
        "black": {"r": 24, "g": 12, "b": 12, "tolerance": 13},
        "dark_blue": {"r": 33, "g": 22, "b": 23, "tolerance": 13},
        "light_blue": {"r": 77, "g": 80, "b": 110, "tolerance": 13},
        "pink": {"r": 145, "g": 33, "b": 57, "tolerance": 13},
    }

    # Détection de la couleur la plus proche parmi celles définies
    detected_color = detect_color(red_value, green_value, blue_value, color_ranges)

    # Affichage de la couleur détectée
    print("***" + detected_color)
