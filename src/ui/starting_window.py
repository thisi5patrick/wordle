from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QVBoxLayout, QWidget

from ..utils.game_settings import ATTEMPTS, LETTERS


class StartingWindow(QHBoxLayout):
    def __init__(self, parent: "MainWindow"):
        super(StartingWindow, self).__init__()
        self.parent = parent

        self.letters = 5
        self.attempts = 6

        self.setStretch(0, 100)
        self.setStretch(3, 100)

        self.insertSpacing(0, 200)
        inner_layout = self._create_inner_layout()

        self.addWidget(inner_layout, 1)
        self.insertSpacing(2, 200)

    def _create_inner_layout(self) -> QWidget:

        font = QFont("Bradley Hand", 24)

        layout = QVBoxLayout()

        letters_label = QLabel("Letters".upper())
        letters_label.setFont(font)
        letters_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(letters_label)

        letters_grid_widget = self._create_letters_num_widget()
        layout.addWidget(letters_grid_widget)

        attempts_label = QLabel("Attempts".upper())
        attempts_label.setFont(font)
        attempts_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(attempts_label)

        attempts_grid_widget = self._create_attempts_num_widget()
        layout.addWidget(attempts_grid_widget)

        layout.addSpacerItem(QSpacerItem(0, 20))

        start_button = QPushButton("Start".upper())
        start_button.setFont(font)
        start_button.clicked.connect(self.start_game)
        layout.addWidget(start_button)

        layout.addSpacerItem(QSpacerItem(0, 20))

        scoreboard_button = QPushButton("Scoreboard".upper())
        scoreboard_button.setFont(font)
        layout.addWidget(scoreboard_button)

        widget = QWidget()
        widget.setLayout(layout)

        return widget

    def start_game(self) -> None:
        self.parent.game_window(self.letters, self.attempts)

    def _add_letter(self) -> None:
        if self.letters >= LETTERS["max"]:
            return
        self.letters += 1
        self.letters_num_label.setText(str(self.letters))

    def _sub_letter(self) -> None:
        if self.letters <= LETTERS["min"]:
            return
        self.letters -= 1
        self.letters_num_label.setText(str(self.letters))

    def _create_letters_num_widget(self) -> QWidget:
        font = QFont("Bradley Hand", 36)

        letters_grid_layout = QGridLayout()
        letters_grid_layout.setVerticalSpacing(5)

        self.letters_num_label = QLabel(str(self.letters))
        self.letters_num_label.setFont(font)
        letters_grid_layout.addWidget(self.letters_num_label, 0, 0, 2, 2)

        more_letters_button = QPushButton("???")
        more_letters_button.clicked.connect(self._add_letter)
        letters_grid_layout.addWidget(more_letters_button, 0, 2, 1, 2)

        less_letters_button = QPushButton("???")
        less_letters_button.clicked.connect(self._sub_letter)
        letters_grid_layout.addWidget(less_letters_button, 1, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(letters_grid_layout)

        return widget

    def _add_attempt(self) -> None:
        if self.attempts >= ATTEMPTS["max"]:
            return
        self.attempts += 1
        self.attempts_num_label.setText(str(self.attempts))

    def _sub_attempt(self) -> None:
        if self.attempts <= ATTEMPTS["min"]:
            return
        self.attempts -= 1
        self.attempts_num_label.setText(str(self.attempts))

    def _create_attempts_num_widget(self) -> QWidget:
        font = QFont("Bradley Hand", 36)

        letters_grid_layout = QGridLayout()
        letters_grid_layout.setVerticalSpacing(5)

        self.attempts_num_label = QLabel(str(self.attempts))
        self.attempts_num_label.setFont(font)
        letters_grid_layout.addWidget(self.attempts_num_label, 0, 0, 2, 2)

        more_attempts_button = QPushButton("???")
        more_attempts_button.clicked.connect(self._add_attempt)
        letters_grid_layout.addWidget(more_attempts_button, 0, 2, 1, 2)

        less_attempts_button = QPushButton("???")
        less_attempts_button.clicked.connect(self._sub_attempt)
        letters_grid_layout.addWidget(less_attempts_button, 1, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(letters_grid_layout)

        return widget
