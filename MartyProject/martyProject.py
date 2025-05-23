from martypy import Marty
import time

MARTY_IP = "192.168.0.108"
marty = None  # Initialisation globale

def connexion():
    global marty
    try:
        print("Connexion réussie à Marty.")
        marty = Marty("wifi", MARTY_IP)
        marty.enable_motors()
        marty.dance()
        time.sleep(2)  # Laisse Marty finir la danse

        capteur_distance()
        battery_detection()
        color_detection()

    except Exception as e:
        print(f"❌ Erreur de connexion : {e}")

def deconnexion():
    global marty
    if marty:
        try:
            marty.close()
            print("✅ Déconnexion réussie.")
        except Exception as e:
            print(f"⚠️ Erreur lors de la déconnexion : {e}")

def capteur_distance():
    try:
        distance = marty.get_obstacle_sensor_reading("right")
        if distance is not None and distance < 20:
            print("⚠️  Obstacle détecté !")
        else:
            print("😊 Aucun obstacle détecté.")
        return distance
    except Exception as e:
        print(f"❌ Erreur capteur distance : {e}")

def color_detection():
    try:
        couleur = marty.get_color_sensor_color("left")
        print(f"🎨✅ Couleur détectée : {couleur}")
        return couleur
    except Exception:
        print("🎨❌ Aucun capteur couleur détecté.")

def battery_detection():
    try:
        battery = marty.get_battery_remaining()
        print(f"🔋 Batterie : {battery}")
        return battery
    except Exception as e:
        print(f"❌ Erreur lecture batterie : {e}")

if __name__ == "__main__":
    connexion()
    deconnexion()
