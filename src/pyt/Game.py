class Game:
    def __init__(self, size):
        self._game_board = [[0 for _ in range(size)] for _ in range(size)]
        self._size = size
        self._score = 0

    def move(self, direction):
        pass

    def set_value(self, x, y, val):
        pass

    def grow_data(self, x, y):
        pass

    def is_finished(self):
        return False

    def empty_tiles(self):
        return 0

    @property
    def board(self):
        return self._game_board

    @property
    def size(self):
        return self._size

    @property
    def score(self):
        return self._score
