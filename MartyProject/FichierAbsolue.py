# -*- coding: utf-8 -*-
"""
Created on Sun Jun 15 19:46:37 2025

@author: Dell
"""

def play_dance_file(self):
    filename = "C:\\users\\Dell\\Desktop\\Nouveau dossier\\circle.dance"
    try:
       with open(filename, 'r') as file:
          lines = [line.strip() for line in file if line.strip()]
      
       if not lines or len(lines) < 2:
          print("Fichier invalide ou vide.")
          return

       # On ignore la première ligne "ABS 5"
       positions = [(int(line[0]), int(line[1])) for line in lines[1:]]

       current_position = positions[0]
       self.controller.stand_up()

       for next_position in positions[1:]:
          dx = next_position[0] - current_position[0]
          dy = next_position[1] - current_position[1]

          # Déplacement avant/arrière (x)
          if dx > 0:
              for _ in range(dx):
                  self.controller.move_forward()
          elif dx < 0:
              for _ in range(-dx):
                  self.controller.move_backward()

          # Déplacement gauche/droite (y)
          if dy > 0:
              for _ in range(dy):
                  self.controller.right_side_step()
          elif dy < 0:
              for _ in range(-dy):
                  self.controller.left_side_step()

          current_position = next_position
          
    except FileNotFoundError:
       print(f"Fichier {filename} non trouvé.")
