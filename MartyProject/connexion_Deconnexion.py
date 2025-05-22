from martypy import Marty

marty = Marty("wifi", "192.168.0.102")


MARTY_IP = "192.168.0.102"



def connexion():
    
    try:
        marty = Marty("wifi", MARTY_IP)
        marty.enable_motors()
        marty.hello()
        marty.dance()
        print("Connexion réussie à Marty.")
    except Exception as e:
        print(f"Erreur de connexion : {e}")


#Cette fonction assure la deconnexion 
def deconnexion():
    global marty
    if marty:
        try:
            marty.close()
            print("Déconnexion réussie.")
        except Exception as e:
            print(f"Erreur lors de la déconnexion : {e}")
    

if __name__ == "__main__":
    connexion()
    input("Appuyez sur Entrée pour se déconnecter...")
    
    deconnexion()
    


