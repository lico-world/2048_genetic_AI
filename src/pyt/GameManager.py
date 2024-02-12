import os
from src.pyt.Game import Game
import random


class GameManager:
    def __init__(self, size, rand=True):
        self._game = Game(size)
        if not rand:  # For reproducible tests
            random.seed(0)

    def game_loop(self, moves_stack=None, verbose=False):
        while not self._game.is_finished():
            if verbose:
                print(self._game)

            if moves_stack is None:
                move = input('play:').upper()
            else:
                move = moves_stack[0]
                moves_stack.pop(0)

            self._game.move(move)

            x = y = 0
            while not self._game.board[x][y] == 0:
                x = random.randint(0, self._game.size-1)
                y = random.randint(0, self._game.size-1)

            self._game.set_value(x, y,
                                 2 if random.randint(1, 100) else 4)
        self.end_game()

    def init_game(self):
        self._game.set_value(random.randint(0, self._game.size-1),
                             random.randint(0, self._game.size-1),
                             2 if random.randint(1, 100) < 90 else 4)

    def end_game(self):
        print('Game over! Final score: ', self._game.score)

    @property
    def game(self):
        return self._game
