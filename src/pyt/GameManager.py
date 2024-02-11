from src.pyt.Game import Game
import random


class GameManager:
    def __init__(self, size, rand=True):
        self._game = Game(size)
        if rand:  # For reproducible tests
            random.seed(0)

    def game_loop(self):
        pass

    def init_game(self):
        pass

    def end_game(self):
        pass
