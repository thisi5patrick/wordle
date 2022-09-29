from PyQt6.QtWidgets import QMainWindow, QWidget, QPushButton
from . import GameWindow, StartingWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Wordle")

    def starting_window(self):
        # self.setFixedSize(700, 500)

        starting_window = StartingWindow()
        widget = QWidget()
        widget.setLayout(starting_window)
        self.setCentralWidget(widget)

    def game_window(self):
        game_window = GameWindow()
        widget = QWidget()
        widget.setLayout(game_window)
        self.setCentralWidget(widget)
