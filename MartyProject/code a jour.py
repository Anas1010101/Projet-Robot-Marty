# Remplace tout ton ancien code par celui-ci

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QPushButton, QLabel,
    QVBoxLayout, QHBoxLayout, QGridLayout, QProgressBar
)
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtCore import QTimer, Qt, QSize

from martypy import Marty


class MartyController:
    def __init__(self):
        self.my_marty = Marty("wifi", "192.168.0.111")

    def connect(self, ip_addr):
        self.my_marty = Marty("wifi", ip_addr)

    def close(self):
        self.my_marty.close()

    def move_forward(self):
        self.my_marty.walk(num_steps=8)
        self.my_marty.stand_straight()

    def move_backward(self):
        self.my_marty.walk(num_steps=8, step_length=-25)
        self.my_marty.stand_straight()

    def right_side_step(self):
        self.my_marty.sidestep("right", 7)
        self.my_marty.stand_straight()

    def left_side_step(self):
        self.my_marty.sidestep("left", 7)
        self.my_marty.stand_straight()

    def turn_right(self):
        self.my_marty.walk(turn=-15)

    def turn_left(self):
        self.my_marty.walk(turn=15)

    def stand_up(self):
        self.my_marty.stand_straight()

    def angry_eyes(self):
        self.my_marty.eyes('angry')

    def excited_eyes(self):
        self.my_marty.eyes('excited')

    def wiggle_eyes(self):
        self.my_marty.eyes('wiggle')

    def normal_eyes(self):
        self.my_marty.eyes('normal')

    def wide_eyes(self):
        self.my_marty.eyes('wide')

    def dance(self):
        self.my_marty.dance()

    def celebrate(self):
        self.my_marty.celebrate()

    def stop(self):
        self.my_marty.stop()

    def distance_sensor(self):
        return self.my_marty.get_distance_sensor()

    def get_color(self):
        hex_color = str(self.my_marty.get_color_sensor_hex("LeftColorSensor"))
        red = int(hex_color[0:2], 16)
        green = int(hex_color[2:4], 16)
        blue = int(hex_color[4:6], 16)

        color_ranges = {
            "red": {"r": 107, "g": 18, "b": 21, "tolerance": 13},
            "green": {"r": 42, "g": 37, "b": 29, "tolerance": 13},
            "yellow": {"r": 240, "g": 94, "b": 50, "tolerance": 13},
            "black": {"r": 19, "g": 10, "b": 8, "tolerance": 13},
            "dark_blue": {"r": 29, "g": 18, "b": 25, "tolerance": 13},
            "light_blue": {"r": 66, "g": 150, "b": 84, "tolerance": 13},
            "pink": {"r": 123, "g": 26, "b": 40, "tolerance": 13},
        }

        for color, values in color_ranges.items():
            if (within_tolerance(red, values["r"], values["tolerance"]) and
                    within_tolerance(green, values["g"], values["tolerance"]) and
                    within_tolerance(blue, values["b"], values["tolerance"])):
                return color
        return "unknown"

    def battery_percentage(self):
        return self.my_marty.get_battery_remaining()


def within_tolerance(value, target, tolerance):
    return abs(value - target) <= tolerance


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Interface Robot Marty")
        self.setFixedSize(800, 400)
        self.setStyleSheet("background-color: #D3D3D3;")

        self.controller = MartyController()

        self.disconnect_button = QPushButton("Déconnecter")
        self.battery_label = QLabel()
        self.battery_progress = QProgressBar()
        self.battery_progress.setRange(0, 100)
        self.battery_progress.setTextVisible(False)
        self.sensor_color_label = QLabel()
        self.sensor_color_square = QLabel()
        self.sensor_color_square.setFixedSize(30, 30)

        self.btn_forward = QPushButton("\u2191")
        self.btn_backward = QPushButton("\u2193")
        self.btn_left = QPushButton("\u2190")
        self.btn_right = QPushButton("\u2192")
        self.btn_turn_left = QPushButton("\u2196")
        self.btn_turn_right = QPushButton("\u2197")

        self.btn_eyes = QPushButton("Set Eyes")
        self.btn_dance = QPushButton("Start Dancing")
        self.btn_celebrate = QPushButton("Start Celebrating")
        self.btn_close = QPushButton("Close")

        control_buttons = [
            self.btn_forward, self.btn_backward, self.btn_left, self.btn_right,
            self.btn_turn_left, self.btn_turn_right
        ]
        for btn in control_buttons:
            btn.setFixedSize(QSize(70, 70))
            btn.setFont(QFont("Arial", 20))
            btn.setStyleSheet("background-color: black; color: white; border-radius: 5px;")

        action_buttons = [self.btn_eyes, self.btn_dance, self.btn_celebrate, self.btn_close]
        for btn in action_buttons:
            btn.setFixedSize(QSize(150, 40))
            btn.setStyleSheet("background-color: #269993; color: white; font-size: 16px; border-radius: 5px;")

        self.disconnect_button.setStyleSheet("background-color: #dc3545; color: white; font-weight: bold;")

        grid_layout = QGridLayout()
        grid_layout.addWidget(self.btn_turn_left, 0, 0)
        grid_layout.addWidget(self.btn_forward, 0, 1)
        grid_layout.addWidget(self.btn_turn_right, 0, 2)
        grid_layout.addWidget(self.btn_left, 1, 0)
        grid_layout.addWidget(self.btn_right, 1, 2)
        grid_layout.addWidget(self.btn_backward, 2, 1)

        action_layout = QVBoxLayout()
        for btn in action_buttons:
            action_layout.addWidget(btn)

        info_layout = QVBoxLayout()
        battery_layout = QHBoxLayout()
        battery_layout.addWidget(self.battery_label)
        battery_layout.addWidget(self.battery_progress)
        color_layout = QHBoxLayout()
        color_layout.addWidget(self.sensor_color_label)
        color_layout.addWidget(self.sensor_color_square)

        info_layout.addWidget(self.disconnect_button)
        info_layout.addLayout(battery_layout)
        info_layout.addLayout(color_layout)

        self.btn_play_dance_file = QPushButton("Jouer fichier .dance")
        self.btn_play_dance_file.setFixedSize(QSize(150, 40))
        action_layout.addWidget(self.btn_play_dance_file)

        main_layout = QHBoxLayout()
        main_layout.addLayout(grid_layout)
        main_layout.addSpacing(50)
        main_layout.addLayout(action_layout)
        main_layout.addSpacing(50)
        main_layout.addLayout(info_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_sensor_values)
        self.timer.start(1000)

        self.disconnect_button.clicked.connect(self.controller.close)
        self.btn_forward.clicked.connect(self.controller.move_forward)
        self.btn_backward.clicked.connect(self.controller.move_backward)
        self.btn_left.clicked.connect(self.controller.left_side_step)
        self.btn_right.clicked.connect(self.controller.right_side_step)
        self.btn_turn_left.clicked.connect(self.controller.turn_left)
        self.btn_turn_right.clicked.connect(self.controller.turn_right)
        self.btn_eyes.clicked.connect(self.controller.angry_eyes)
        self.btn_dance.clicked.connect(self.controller.dance)
        self.btn_celebrate.clicked.connect(self.controller.celebrate)
        self.btn_close.clicked.connect(self.close)
        self.btn_play_dance_file.clicked.connect(self.play_dance_file)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Z:
            self.controller.move_forward()
        elif event.key() == Qt.Key.Key_S:
            self.controller.move_backward()
        elif event.key() == Qt.Key.Key_Q:
            self.controller.left_side_step()
        elif event.key() == Qt.Key.Key_D:
            self.controller.right_side_step()

    def update_sensor_values(self):
        battery = self.controller.battery_percentage()
        self.battery_label.setText(f"Battery: {battery}%")
        self.battery_progress.setValue(battery)

        if battery >= 70:
            self.battery_progress.setStyleSheet("QProgressBar::chunk { background-color: #4CAF50; }")
        elif battery >= 30:
            self.battery_progress.setStyleSheet("QProgressBar::chunk { background-color: #FFC107; }")
        else:
            self.battery_progress.setStyleSheet("QProgressBar::chunk { background-color: #F44336; }")

        color = self.controller.get_color()
        self.sensor_color_label.setText(f"Couleur : {color}")
        self.sensor_color_square.setStyleSheet(f"background-color: {QColor(color).name()};")

        if color == "green":
            self.controller.dance()
        elif color == "black":
            self.controller.celebrate()

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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
