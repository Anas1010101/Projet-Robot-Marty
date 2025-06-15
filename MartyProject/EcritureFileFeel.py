def write_feel_file(path, data):
    """
    Écrit un fichier .feel contenant des lignes au format :
        couleur;émotion;code_hex

    Exemple :
        blue;calm;#0000FF
    """
    with open(path, "w", encoding="utf-8") as file:
        for color, info in data.items():
            emotion = info.get("emotion", "")
            hex_code = info.get("hex_code", "")
            file.write(f"{color};{emotion};{hex_code}\n")
            
def write_dance_file(path, data):
    """
    Écrit un fichier .dance (mode SEQ) à partir d’un dictionnaire contenant :
        - mode : "SEQ"
        - param : entier
        - commands : liste de tuples (nb_mouvements, direction)
    
    Exemple de contenu généré :
        SEQ 2
        3L
        2R
        1U
    """
    if data.get("mode") != "SEQ" or "commands" not in data:
        raise ValueError("Le format du dictionnaire est invalide ou le mode n'est pas SEQ")

    with open(path, "w", encoding="utf-8") as file:
        file.write(f"{data['mode']} {data['param']}\n")
        for nb, direction in data["commands"]:
            file.write(f"{nb}{direction}\n")            
            
            
            
            
            
            
            
            
            