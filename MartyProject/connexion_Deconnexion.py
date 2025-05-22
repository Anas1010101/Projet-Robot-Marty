from martypy import Marty

MARTY_IP = "192.168.0.102"

def connexion():
    try:
        marty = Marty("wifi", MARTY_IP)
        marty.dance()
        print("Connexion Réussie à Marty.")
    except Exception as e:
        print(f"Erreur de connexion : {e}")

if __name__ == "__main__":
    connexion()

    