def _isValidValue(x):
    if x == 0:
        return True  # Because an empty tile is a 0
    elif x == 1:
        return False
    while x != 1:
        if x % 2 != 0:
            return False
        x = x // 2
    return True


class Game:
    def __init__(self, size):
        self._game_board = [[0 for _ in range(size)] for _ in range(size)]
        self._size = size
        self._score = 0

    def move(self, direction):
        pass

    def set_value(self, x, y, val):
        if _isValidValue(val):
            self._game_board[x][y] = val
        else:
            raise ValueError

    def grow_data(self, x, y):
        if self._game_board[x][y] == 0:
            raise ValueError
        self.set_value(x, y, self._game_board[x][y] * 2)

    def is_finished(self):
        return False

    def empty_tiles(self):
        count = 0
        for raw in self._game_board:
            for val in raw:
                if val == 0:
                    count += 1
        return count

    @property
    def board(self):
        return self._game_board

    @property
    def size(self):
        return self._size

    @property
    def score(self):
        return self._score
