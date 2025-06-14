def read_file_feels(content):
    """
    Analyse une chaîne de caractères représentant un fichier de sentiments liés aux couleurs.
    Chaque ligne doit être au format : couleur;émotion;code_hexadécimal

    Exemple de ligne :
        blue;calm;#0000FF

    Retourne un dictionnaire du type :
    {
        "blue": {"emotion": "calm", "hex_code": "#0000FF"},
        ...
    }
    """
    lines = content.strip().split("\n")  # On découpe chaque ligne du fichier
    data = {}

    for line in lines:
        if line.strip():  # Ignore les lignes vides
            parts = line.split(';')  # On s'attend à 3 éléments séparés par ;
            if len(parts) == 3:
                color, emotion, hex_code = parts
                data[color.strip()] = {
                    "emotion": emotion.strip(),
                    "hex_code": hex_code.strip()
                }

    return data

def process_file_feels(path):
    """
    Ouvre un fichier texte situé à l’emplacement 'path',
    lit son contenu, puis le transforme en dictionnaire avec read_file_feels().

    Retourne un dictionnaire avec les couleurs, émotions et codes hexadécimaux.
    """
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()

    return read_file_feels(content)

def get_emotion_by_color(data_dict, color):
    """
    Retourne l’émotion associée à une couleur donnée.
    Si la couleur n’existe pas, retourne None.
    """
    return data_dict.get(color, {}).get('emotion', None)

