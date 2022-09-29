from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QPushButton,
    QLabel,
    QHBoxLayout,
    QSpacerItem,
    QVBoxLayout,
    QWidget,
    QGridLayout,
)


class StartingWindow(QHBoxLayout):
    def __init__(self):
        super(StartingWindow, self).__init__()
        self.LETTERS = 5
        self.ATTEMPTS = 5

        self.setStretch(0, 100)
        self.setStretch(3, 100)

        self.insertSpacing(0, 200)
        inner_layout = self._create_inner_layout()

        self.addWidget(inner_layout, 1)
        self.insertSpacing(2, 200)

    def _create_inner_layout(self):

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
        layout.addWidget(start_button)

        layout.addSpacerItem(QSpacerItem(0, 20))

        scoreboard_button = QPushButton("Scoreboard".upper())
        scoreboard_button.setFont(font)
        layout.addWidget(scoreboard_button)

        widget = QWidget()
        widget.setLayout(layout)

        return widget

    def _create_letters_num_widget(self) -> QWidget:
        font = QFont("Bradley Hand", 36)

        letters_grid_layout = QGridLayout()
        letters_grid_layout.setVerticalSpacing(5)

        letters_num_label = QLabel(str(self.LETTERS))
        letters_num_label.setFont(font)
        letters_grid_layout.addWidget(letters_num_label, 0, 0, 2, 2)

        more_letters_button = QPushButton("ᐱ")
        letters_grid_layout.addWidget(more_letters_button, 0, 2, 1, 2)

        less_letters_button = QPushButton("ᐯ")
        letters_grid_layout.addWidget(less_letters_button, 1, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(letters_grid_layout)

        return widget

    def _create_attempts_num_widget(self) -> QWidget:
        font = QFont("Bradley Hand", 36)

        letters_grid_layout = QGridLayout()
        letters_grid_layout.setVerticalSpacing(5)

        letters_num_label = QLabel(str(self.ATTEMPTS))
        letters_num_label.setFont(font)
        letters_grid_layout.addWidget(letters_num_label, 0, 0, 2, 2)

        more_letters_button = QPushButton("ᐱ")
        letters_grid_layout.addWidget(more_letters_button, 0, 2, 1, 2)

        less_letters_button = QPushButton("ᐯ")
        letters_grid_layout.addWidget(less_letters_button, 1, 2, 1, 2)

        widget = QWidget()
        widget.setLayout(letters_grid_layout)

        return widget
