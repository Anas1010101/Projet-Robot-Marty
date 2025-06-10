from time import sleep

from martypy import Marty

def hex_to_rgb(hex_color):
    red = int(hex_color[0:2], 16)
    green = int(hex_color[2:4], 16)
    blue = int(hex_color[4:6], 16)
    return red, green, blue


def within_tolerance(value, target, tolerance):
    return abs(value - target) <= tolerance


def detect_color(r, g, b, color_ranges):
    for color, values in color_ranges.items():
        if (within_tolerance(r, values["r"], values["tolerance"]) and
                within_tolerance(g, values["g"], values["tolerance"]) and
                within_tolerance(b, values["b"], values["tolerance"])):
            return color
    return "unknown"


marty = Marty("wifi", "192.168.0.103")
marty.set_blocking(False)

marty.stand_straight()
while True:
    sleep(2)
    hex_color = str(marty.get_color_sensor_hex("LeftColorSensor"))

    red_value, green_value, blue_value = hex_to_rgb(hex_color)
    print(f"Red: {red_value} | Green: {green_value} | Blue: {blue_value}")

    # Valeurs de référence pour les couleurs
    color_ranges = {
        "red": {"r": 126, "g": 23, "b": 33, "tolerance": 13},
        "green": {"r": 46, "g": 43, "b": 40, "tolerance": 13},
        "yellow": {"r": 17, "g": 103, "b": 5, "tolerance": 13},
        "black": {"r": 24, "g": 12, "b": 12, "tolerance": 13},
        "dark_blue": {"r": 33, "g": 22, "b": 23, "tolerance": 13},
        "light_blue": {"r": 77, "g": 80, "b": 110, "tolerance": 13},
        "pink": {"r": 145, "g": 33, "b": 57, "tolerance": 13},
    }

    detected_color = detect_color(red_value, green_value, blue_value, color_ranges)
    print("***" + detected_color)