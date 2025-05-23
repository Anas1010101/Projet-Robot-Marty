from martypy import Marty
import time

marty = Marty("wifi", "192.168.0.102")


MARTY_IP = "192.168.0.102"



def connexion():
    
    try:
        print("Connexion réussie à Marty.")
        marty = Marty("wifi", MARTY_IP)
        marty.enable_motors()
        marty.hello()
        marty.dance()

        capteur()
        
    except Exception as e:
        print(f"Erreur de connexion : {e}")


#Cette fonction assure la deconnexion 
def deconnexion():
    global marty
    if marty:
        try:
            marty.close()
            print("✅ Déconnexion réussie.")
        except Exception as e:
            print(f"⚠️ Erreur lors de la déconnexion : {e}")

def capteur():
    global marty
    battery = marty.get_battery_remaining()
    distance = marty.get_obstacle_sensor_reading("right")

    #Cette partie du code va afficher si il y a un obstacle sur la route de Marty à travers son pieds droit
    if distance is not None and distance < 20:
        print("⚠️  Obstacle détecté !")
    else:
        print("😊 Aucun obstacle détecté.")

    #Cette partie du code va afficher le niveau de batterie de Marty
    print(f"🔋 Batterie : {battery}")

    #Cette partie du code va afficher la couleur captée par le pied gauche de Marty
    try:
        couleur = marty.get_color_sensor_color("left")
        print(f"🎨✅ Couleur détectée : {couleur}")
    except Exception:
        print("🎨❌ Aucun capteur couleur détecté.")

    
    
    

if __name__ == "__main__":
    connexion()
    
    deconnexion()
    
    
    


