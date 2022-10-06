from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QPalette
from PyQt6.QtWidgets import QGridLayout, QLabel, QPushButton

from .. import Color


class GridInput(QLabel):
    def __init__(self, palette: QPalette, font: QFont):
        super(GridInput, self).__init__()
        self.setFixedSize(100, 100)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.setFont(font)


class GameWindow(QGridLayout):
    def __init__(self, letters: int, attempts: int):
        super(GameWindow, self).__init__()
        self.setSpacing(2)
        self.letters = letters
        self.attempts = attempts
        self._create_inputs()
        self._create_placeholder()
        self._create_function_buttons()

    def _create_placeholder(self) -> None:
        self.spacerItem()
        message_info = QLabel()
        message_info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message_info.setAutoFillBackground(True)
        font = QFont()
        font.setPixelSize(20)
        message_info.setFont(font)
        self.addWidget(message_info, self.attempts + 1, 0, 2, self.letters)

    def _create_function_buttons(self) -> None:
        button_size = QSize(0, 50)
        font = QFont("Bradley Hand", 24)

        self.spacerItem()

        restart_button = QPushButton()
        restart_button.setText("Restart Game")
        restart_button.setMinimumSize(button_size)
        restart_button.setFont(font)
        self.addWidget(restart_button, self.attempts + 3, 0, 1, 2)

        return_button = QPushButton()
        return_button.setText("Return")
        return_button.setMinimumSize(button_size)
        return_button.setFont(font)
        self.addWidget(return_button, self.attempts + 3, self.letters - 2, 1, 2)

    def _create_inputs(self) -> None:
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, Color.DEFAULT.value)
        font = QFont()
        font.setCapitalization(QFont.Capitalization.AllUppercase)
        font.setBold(True)
        font.setPixelSize(70)
        for attempt_num in range(self.attempts):
            for letter_num in range(self.letters):
                input = GridInput(palette, font)
                self.addWidget(input, attempt_num, letter_num)
