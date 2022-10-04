from functools import wraps
from string import ascii_uppercase
from typing import Callable

from PyQt6 import QtGui
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QPushButton, QWidget

from . import GameWindow, StartingWindow
from .app import GameLogic


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Wordle")

    def set_window_location(func: Callable):
        @wraps(func)
        def inner(self, *args, **kwargs):
            func_ex = func(self, *args, **kwargs)
            w = self.width()
            h = self.height()
            screen_w = self.screen().size().width()
            screen_h = self.screen().size().height()
            self.setGeometry(screen_w / 2 - w / 2, screen_h / 2 - h / 2, w, h)
            return func_ex
        return inner

    @set_window_location
    def starting_window(self):
        self.starting_window_view = StartingWindow(self)
        widget = QWidget()
        widget.setLayout(self.starting_window_view)

        self.setFixedSize(self.starting_window_view.sizeHint())
        self.setCentralWidget(widget)

    @set_window_location
    def game_window(self, letters: int, attempts: int):
        game_window_view = GameWindow(letters, attempts)

        exit_button: QPushButton = game_window_view.itemAt(game_window_view.count() - 1).widget()
        exit_button.clicked.connect(self._exit_game)

        restart_button: QPushButton = game_window_view.itemAt(game_window_view.count() - 2).widget()
        restart_button.clicked.connect(self._restart_game)

        self.game_logic = GameLogic(letters, attempts, game_window_view)
        self.game_logic.start_game()

        widget = QWidget()
        widget.setLayout(game_window_view)
        self.setFixedSize(game_window_view.sizeHint())
        self.setCentralWidget(widget)

    def _exit_game(self):
        self.starting_window()

    def _restart_game(self):
        self.starting_window_view.start_game()

    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        if event.key() == Qt.Key.Key_Backspace:
            self.game_logic.remove_letter()
        if event.key() == Qt.Key.Key_Return:
            self.game_logic.check_word()

        key = event.text().upper()
        if key in ascii_uppercase:
            self.game_logic.add_letter(key)
