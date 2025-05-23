from  martypy import Marty

my_marty=Marty ("wifi","192.168.0.53")

## Detect one Obstacle

def obstacle_detecte ():
    value=my_marty.foot_obstacle_sensed()
    
    print(f"Est ce que l'obstacle est detecté ?",value) # Affiche True si l'obstacle est détecté et False si l'obstacle est détecté


    

def distance_obstacle():

    distance=my_marty.get_distance_sensor() ## Récupère la distance en mm
    print("La distance par rapport au capteur est de ",distance,"mm")

def battery_level():
    level_battery=my_marty.get_battery_remaining() 

    print("Le niveau de batterie {level_battery}") 

  ##1)Detection of Values on Color Sensor
def detect_color_on_leftFootCS():
    valeur_1=my_marty.get_ground_sensor_reading('LeftColorSensor')
    print("Capteur Pied gauche:",valeur_1) ##The more the surface is clear(white) the more the value is huge 


def detect_color_on_rightFootCS():
    valeur_2=my_marty.get_ground_sensor_reading('RightColorSensor')
    print("Capteur Pied droit:",valeur_2)## La fonction me renvoi une valeur numérique

 ##2)Detection of Values on IR Sensor


 
def detect_color_on_leftFootIR():
    valeur_a=my_marty.get_ground_sensor_reading('LeftIRFoot')
    print("Capteur Pied gauche:",valeur_a)


def detect_color_on_rightFootIR():
    valeur_b=my_marty.get_ground_sensor_reading('RightIRFoot')
    print("Capteur Pied gauche:",valeur_b)




