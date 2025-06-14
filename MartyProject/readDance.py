def readFileDance(content):
    """
    Analyse le contenu d'un fichier texte décrivant une séquence de mouvements de danse.

    Returns un dictionnaire contenant :
        - mode (ex : 'SEQ')
        - param (paramètre associé)
        - commands (liste de tuples : (nb_mouvements, direction))
        - type (ex : 'sequence')
    """
    lines = content.strip().split('\n')

    if not lines or len(lines[0].split()) < 2:
        raise ValueError("En-tête invalide : il manque le mode ou le paramètre")

    header = lines[0].split()
    mode = header[0]
    try:
        param = int(header[1])
    except ValueError:
        raise ValueError("Le paramètre n'est pas un entier valide")

    movements = []
    if mode == "SEQ":
        for line in lines[1:]:
            line = line.strip()
            if not line or len(line) < 2:
                continue
            try:
                nb_movements = int(line[0])
                direction = line[1].upper()
                if direction in {"L", "R", "U", "B"}:
                    movements.append((nb_movements, direction))
            except (ValueError, IndexError):
                continue

    return {
        "mode": mode,
        "param": param,
        "commands": movements,
        "type": "sequence"
    }

def extractMovements(content):
    """
    Retourne uniquement la liste des mouvements à partir du contenu texte.
    """
    data = readFileDance(content)
    return data["commands"] if data["mode"] == "SEQ" else []