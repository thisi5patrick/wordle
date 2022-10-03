import random
from pathlib import Path

import numpy as np

from . import Color


class GameLogic:
    def __init__(self, letters: int, attempts: int, game_inputs: np.array):
        self.letters = letters
        self.attempts = attempts
        self.game_inputs = game_inputs
        self._load_all_words()
        self.checked_word = ""

    def _load_all_words(self):
        word_path = Path(__file__).parent.resolve().joinpath("words.txt")
        with open(word_path) as f:
            words = f.readlines()
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
        self.checked_word += letter

    def remove_letter(self):
        self.checked_word = self.checked_word[:-1]

    def check_word(self):
        print(self.checked_word)

    @staticmethod
    def check_letter_in_word(word: str, letter: str, position: int) -> Color:
        if word[position] == letter:
            return Color.GREEN
        if letter in word:
            return Color.YELLOW
        return Color.RED
