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

          

def obstacle_detectection():
    value=marty.foot_obstacle_sensed()

    print(f"Est ce que l'obstacle est detecté ?",value) # Affiche True si l'obstacle est détecté et False si l'obstacle est détecté
    distance=marty.get_distance_sensor() ## Récupère la distance en mm
    print("La distance par rapport au capteur est de ",distance,"mm")

def distance_obstacle():

    distance=marty.get_distance_sensor() ## Récupère la distance en mm
    print("La distance par rapport au capteur est de ",distance,"mm")

def color_detection_left():
    valeur_1=marty.get_ground_sensor_reading('LeftColorSensor')
    print("Capteur Pied gauche:",valeur_1) ##The more the surface is clear(white) the more the value is huge 

def color_detection_right():
    valeur_2=marty.get_ground_sensor_reading('RightColorSensor')
    print("Capteur Pied droit:",valeur_2)## La fonction me renvoi une valeur numérique


    


    
    

if __name__ == "__main__":
    connexion()
    obstacle_detectection()
    distance_obstacle()
    color_detection_left()
    color_detection_right()
    
    deconnexion()
    
