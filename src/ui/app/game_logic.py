import random
from pathlib import Path

import numpy as np
from PyQt6.QtGui import QPalette

from . import Color


class GameLogic:
    def __init__(self, letters: int, attempts: int, game_inputs: np.array):
        self.letters = letters
        self.attempts = attempts
        self.attempt = 0
        self.letter = 0
        self.game_inputs = game_inputs
        self._load_all_words()
        self.checked_word = ""

    def _load_all_words(self):
        word_path = Path(__file__).parent.resolve().joinpath("words.txt")
        with open(word_path) as f:
            words = f.readlines()
        words = [word[:-1].upper() for word in words]
        self._words = words

    def select_word(self):
        potential_words = []
        for word in self._words:
            word = word[:-1]
            if len(word) == self.letters:
                potential_words.append(word)

        return random.choice(potential_words)

    def start_game(self):
        self.word = self.select_word()

    def add_letter(self, letter):
        if self.letter >= self.letters:
            return
        self.game_inputs[self.attempt][self.letter].setText(letter)
        self.letter += 1
        self.checked_word += letter

    def remove_letter(self):
        if self.letter <= 0:
            return
        self.letter -= 1
        self.game_inputs[self.attempt][self.letter].setText("")
        self.checked_word = self.checked_word[:-1]

    def check_word(self):
        if self.letter != self.letters:
            return

        if not self._word_exists():
            print("Word does not exist")
            return
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

    def _word_exists(self):
        print(self.checked_word)
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
