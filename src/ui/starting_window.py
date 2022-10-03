from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGridLayout, QHBoxLayout, QLabel, QPushButton, QSpacerItem, QVBoxLayout, QWidget


class StartingWindow(QHBoxLayout):
    def __init__(self, parent: "MainWindow"):
        super(StartingWindow, self).__init__()
        self.parent = parent
        self.LETTERS = {"min": 5, "max": 12, "letters": 5}
        self.ATTEMPTS = {"min": 5, "max": 12, "attempts": 6}

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
        start_button.clicked.connect(self._start_game)
        layout.addWidget(start_button)

        layout.addSpacerItem(QSpacerItem(0, 20))

        scoreboard_button = QPushButton("Scoreboard".upper())
        scoreboard_button.setFont(font)
        layout.addWidget(scoreboard_button)

        widget = QWidget()
        widget.setLayout(layout)

        return widget

    def _start_game(self) -> None:
        self.parent.game_window(self.LETTERS["letters"], self.ATTEMPTS["attempts"])

    def _add_letter(self) -> None:
        if self.LETTERS["letters"] >= self.LETTERS["max"]:
            return
        self.LETTERS["letters"] += 1
        self.letters_num_label.setText(str(self.LETTERS["letters"]))

    def _sub_letter(self) -> None:
        if self.LETTERS["letters"] <= self.LETTERS["min"]:
            return
        self.LETTERS["letters"] -= 1
        self.letters_num_label.setText(str(self.LETTERS["letters"]))

    def _create_letters_num_widget(self) -> QWidget:
        font = QFont("Bradley Hand", 36)

        letters_grid_layout = QGridLayout()
        letters_grid_layout.setVerticalSpacing(5)

        self.letters_num_label = QLabel(str(self.LETTERS["letters"]))
        self.letters_num_label.setFont(font)
        letters_grid_layout.addWidget(self.letters_num_label, 0, 0, 2, 2)

        more_letters_button = QPushButton("ᐱ")
        more_letters_button.clicked.connect(self._add_letter)
        letters_grid_layout.addWidget(more_letters_button, 0, 2, 1, 2)

        less_letters_button = QPushButton("ᐯ")
        less_letters_button.clicked.connect(self._sub_letter)
        letters_grid_layout.addWidget(less_letters_button, 1, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(letters_grid_layout)

        return widget

    def _add_attempt(self) -> None:
        if self.ATTEMPTS["attempts"] >= self.ATTEMPTS["max"]:
            return
        self.ATTEMPTS["attempts"] += 1
        self.attempts_num_label.setText(str(self.ATTEMPTS["attempts"]))

    def _sub_attempt(self) -> None:
        if self.ATTEMPTS["attempts"] <= self.ATTEMPTS["min"]:
            return
        self.ATTEMPTS["attempts"] -= 1
        self.attempts_num_label.setText(str(self.ATTEMPTS["attempts"]))

    def _create_attempts_num_widget(self) -> QWidget:
        font = QFont("Bradley Hand", 36)

        letters_grid_layout = QGridLayout()
        letters_grid_layout.setVerticalSpacing(5)

        self.attempts_num_label = QLabel(str(self.ATTEMPTS["attempts"]))
        self.attempts_num_label.setFont(font)
        letters_grid_layout.addWidget(self.attempts_num_label, 0, 0, 2, 2)

        more_attempts_button = QPushButton("ᐱ")
        more_attempts_button.clicked.connect(self._add_attempt)
        letters_grid_layout.addWidget(more_attempts_button, 0, 2, 1, 2)

        less_attempts_button = QPushButton("ᐯ")
        less_attempts_button.clicked.connect(self._sub_attempt)
        letters_grid_layout.addWidget(less_attempts_button, 1, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(letters_grid_layout)

        return widget
