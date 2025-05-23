from martypy import Marty

my_marty=Marty ("wifi","192.168.0.53")


valeur_1=my_marty.get_ground_sensor_reading('LeftColorSensor')
valeur_2=my_marty.get_ground_sensor_reading('LeftIRFoot')

def marty_happy(): ##Ici pour faire la detection j'utilise le capteur sur le pied gauche



    if valeur_1 =="couleur_verte_Color_sensor" and valeur_2=="coueleur_verte_color_IR":  ## Couleur_verte c'est la valeur qu'on détecter avec le  capteur ,puis on va juste remplacer dans ce code  
    
       my_marty.eyes(pose_or_angle='exicited',move_time=2000)

def marty_angry():



    
    if valeur_1 =="couleur_rouge_Color_sensor" and valeur_2=="couleur_rouge_color_IR":

     my_marty.eyes(pose_or_angle='angry',move_time=2000)

def marty_normal():
    my_marty.eyes(pose_or_angle='normal',move_time=2000)

    

