import os
from src.pyt.Game import Game
import random


class GameManager:
    def __init__(self, size, rand=True):
        self._game = Game(size)
        if not rand:  # For reproducible tests
            random.seed(0)

    def game_loop(self, verbose=False, moves_stack=None):
        wait_end = moves_stack is None
        if not wait_end:
            stack = list(moves_stack)

        while (not self._game.is_finished()) if wait_end else len(stack) > 0:
            if verbose:
                print(self._game)

            if wait_end:
                move = input('play:').upper()
            else:
                move = stack[0]
                stack.pop(0)

            self._game.move(move)

            x = random.randint(0, self._game.size-1)
            y = random.randint(0, self._game.size-1)
            while not self._game.board[x][y] == 0:
                x = random.randint(0, self._game.size-1)
                y = random.randint(0, self._game.size-1)

            self._game.set_value(x, y,
                                 2 if random.randint(1, 100) else 4)
        self.end_game(verbose)

    def init_game(self):
        self._game.set_value(random.randint(0, self._game.size-1),
                             random.randint(0, self._game.size-1),
                             2 if random.randint(1, 100) < 90 else 4)

    def end_game(self, verbose):
        if verbose:
            print('Game over! Final score: ', self._game.score)

    @property
    def game(self):
        return self._game
