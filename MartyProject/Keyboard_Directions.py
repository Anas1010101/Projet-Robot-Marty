import sys
from PyQt6.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from Marty_Detection import move_on
from Marty_Detection import move_back
from Marty_Detection import step_right
from Marty_Detection import step_left



class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test des touches")
        self.resize(400, 100)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

def keyPressEvent(event):
    if event.key() == Qt.Key.Key_Z:
        ##J'appelle la fonction dans un autre fichier 
        move_on()
    elif event.key() == Qt.Key.Key_S:
        move_back()
    elif event.key() == Qt.Key.Key_Q:
        step_right()
    elif event.key() == Qt.Key.Key_D:
        step_left()
    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())

