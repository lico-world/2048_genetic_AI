def _isValidValue(x):
    if x == 0:
        return True  # Because an empty tile is a 0
    elif x == 1:
        return False
    while x != 1:
        if x % 2 != 0:
            return False
        x = x // 2
    return True  # Return if the non 0 or 1 value is a power of 2


class Game:
    def __init__(self, size):
        self._game_board = [[0 for _ in range(size)] for _ in range(size)]
        self._size = size
        self._score = 0

    def move(self, direction):
        if direction == 'U':  # UP
            for y in range(self._size-1, 0, -1):
                for x in range(self._size):
                    if self._game_board[x][y-1] == 0:
                        self.set_value(x, y-1, self._game_board[x][y])
                        self.set_value(x, y, 0)
                    elif self._game_board[x][y-1] == self._game_board[x][y]:
                        self.grow_data(x, y-1)
                        self.set_value(x, y, 0)
        elif direction == 'D':  # DOWN
            for y in range(self._size-1):
                for x in range(self._size):
                    if self._game_board[x][y+1] == 0:
                        self.set_value(x, y+1, self._game_board[x][y])
                        self.set_value(x, y, 0)
                    elif self._game_board[x][y+1] == self._game_board[x][y]:
                        self.grow_data(x, y+1)
                        self.set_value(x, y, 0)
        elif direction == 'R':  # RIGHT
            for x in range(self._size-1):
                for y in range(self._size):
                    if self._game_board[x+1][y] == 0:
                        self.set_value(x+1, y, self._game_board[x][y])
                        self.set_value(x, y, 0)
                    elif self._game_board[x+1][y] == self._game_board[x][y]:
                        self.grow_data(x+1, y)
                        self.set_value(x, y, 0)
        elif direction == 'L':  # LEFT
            for x in range(self._size-1, 0, -1):
                for y in range(self._size):
                    if self._game_board[x-1][y] == 0:
                        self.set_value(x-1, y, self._game_board[x][y])
                        self.set_value(x, y, 0)
                    elif self._game_board[x-1][y] == self._game_board[x][y]:
                        self.grow_data(x-1, y)
                        self.set_value(x, y, 0)
        else:
            raise ValueError  # The move direction cannot be anything else than up/down/right/left

    def set_value(self, x, y, val):
        if _isValidValue(val):
            self._game_board[x][y] = val
        else:
            raise ValueError

    def grow_data(self, x, y):
        if self._game_board[x][y] == 0:
            raise ValueError  # Trying to grow an empty tile would be the result of a bad behavior
        self.set_value(x, y, self._game_board[x][y] * 2)

    def is_finished(self):
        if self.empty_tiles() > 0:
            return False  # If any tile still empty the game cannot be over

        possible = False
        for x in range(self._size):
            for y in range(self._size):
                if x > 0:
                    possible |= (self._game_board[x][y] == self._game_board[x - 1][y])
                if x < self._size - 1:
                    possible |= (self._game_board[x][y] == self._game_board[x + 1][y])
                if y > 0:
                    possible |= (self._game_board[x][y] == self._game_board[x][y - 1])
                if y < self._size - 1:
                    possible |= (self._game_board[x][y] == self._game_board[x][y + 1])
        return not possible  # not because if any move possible -> the game is not finished

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
        count = 0
        for row in self._game_board:
            for val in row:
                count += val
        return count

    def __str__(self):
        str_val = ''
        for y in range(self._size):
            for x in range(self._size):
                str_val += str(self._game_board[x][y])
            str_val += '\n'
        return str_val
