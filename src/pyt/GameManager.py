import os
from src.pyt.Game import Game
import random


class GameManager:
    def __init__(self, size, rand=True):
        self._game = Game(size)
        if not rand:  # For reproducible tests
            random.seed(0)

        self._n = [[0 for _ in range(size)] for _ in range(size)]

    def game_loop(self, verbose=False, moves_stack=None):
        use_stack = moves_stack is not None
        if use_stack:
            stack = list(moves_stack)

        while (not self._game.is_finished()) if not use_stack else len(stack) > 0:
            if verbose:
                print(self._game)

            if not use_stack:
                move = input('play:').upper()
            else:
                move = stack[0]
                stack.pop(0)

            if move == 'Z':
                for i, row in enumerate(self._n):
                    for j, val in enumerate(row):
                        self._game.set_value(i, j, val)
                continue

            for i, row in enumerate(self._game.board):
                for j, val in enumerate(row):
                    self._n[i][j] = val

            wrong_move = False
            try:
                self._game.move(move)
            except ValueError:
                wrong_move = True

            if not self._n == self._game.board or not wrong_move:
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

        for i, row in enumerate(self._game.board):
            for j, val in enumerate(row):
                self._n[i][j] = val

    def end_game(self, verbose):
        if verbose:
            print('Game over! Final score: ', self._game.score)

    @property
    def game(self):
        return self._game
