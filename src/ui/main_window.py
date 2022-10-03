from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget

from string import ascii_uppercase

from . import GameWindow, StartingWindow
from .app import GameLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Wordle")

    def starting_window(self):
        starting_window = StartingWindow(self)
        widget = QWidget()
        widget.setLayout(starting_window)
        self.setCentralWidget(widget)

    def game_window(self, letters: int, attempts: int):
        game_window = GameWindow(letters, attempts)
        game_inputs = game_window.get_inputs()

        self.game_logic = GameLogic(letters, attempts, game_inputs)
        self.game_logic.start_game()

        widget = QWidget()
        widget.setLayout(game_window)
        self.setFixedSize(game_window.sizeHint())
        self.setCentralWidget(widget)

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Backspace:
            self.game_logic.remove_letter()
        if event.key() == Qt.Key.Key_Return and len(self.game_logic.checked_word) == self.game_logic.letters:
            self.game_logic.check_word()

        key = event.text().upper()
        if key in ascii_uppercase:
            if len(self.game_logic.checked_word) >= self.game_logic.letters:
                return
            self.game_logic.add_letter(key)



