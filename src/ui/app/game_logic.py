import random
from pathlib import Path

import numpy as np
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QGridLayout, QLabel

from . import Color


class GameLogic:
    def __init__(self, letters: int, attempts: int, game_window: QGridLayout):
        self.letters = letters
        self.attempts = attempts
        self.attempt = 0
        self.letter = 0
        self.game_window = game_window
        self.game_inputs = np.array([game_window.itemAt(item).widget() for item in range(attempts * letters)]).reshape(
            [attempts, letters]
        )
        self._load_all_words()
        self.checked_word = ""
        self.placeholder = self._get_placeholder()

    def _get_placeholder(self) -> QLabel:
        return self.game_window.itemAt(self.letters * self.attempts).widget()

    def _load_all_words(self) -> None:
        word_path = Path(__file__).parent.resolve().joinpath("words.txt")
        with open(word_path) as f:
            words = f.readlines()
        words = [word[:-1].upper() for word in words]
        self._words = tuple(words)

    def select_word(self) -> str:
        potential_words = []
        for word in self._words:
            word = word[:-1]
            if len(word) == self.letters:
                potential_words.append(word)

        return random.choice(potential_words)

    def start_game(self) -> None:
        self.word = self.select_word()

    def add_letter(self, letter) -> None:
        if self.letter >= self.letters:
            return
        self.game_inputs[self.attempt][self.letter].setText(letter)
        self.letter += 1
        self.checked_word += letter

    def remove_letter(self) -> None:
        if self.letter <= 0:
            return
        self.letter -= 1
        self.game_inputs[self.attempt][self.letter].setText("")
        self.checked_word = self.checked_word[:-1]

    def check_word(self) -> None:
        if self.letter != self.letters:
            return

        if not self._word_exists():
            self.placeholder.setText("Word does not exist")
            return
        self.placeholder.clear()
        palette = QPalette()
        game_won = True
        for idx, letter in enumerate(self.checked_word):
            color = self._check_letter_in_word(letter, idx)
            if color != Color.GREEN:
                game_won = False
            palette.setColor(QPalette.ColorRole.Window, color.value)
            self.game_inputs[self.attempt][idx].setPalette(palette)
        if game_won:
            self._game_won()
            return
        self.attempt += 1
        self.letter = 0
        self.checked_word = ""

    def _game_won(self):
        ...

    def _game_lost(self):
        ...

    def _word_exists(self) -> bool:
        for word in self._words:
            if word.upper() == self.checked_word:
                return True
        return False

    def _check_letter_in_word(self, letter: str, position: int) -> Color:
        if self.word[position] == letter:
            return Color.GREEN
        if letter in self.word:
            return Color.YELLOW
        return Color.RED
