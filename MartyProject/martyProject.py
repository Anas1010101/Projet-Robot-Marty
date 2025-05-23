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
        marty.play_mp3("soundLinga.mp3")

        
        
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


    
    
    

if __name__ == "__main__":
    connexion()
    
    deconnexion()
    
    
    


