import unittest
from src.pyt.Game import *


class TestGame(unittest.TestCase):
    def setUp(self):
        self._game = Game(4)
        self._test_array = [[0 for _ in range(4)] for _ in range(4)]

    def test_init(self):
        self.assertEqual(self._test_array, self._game.board)

    def test_set_value(self):
        self._test_array[0][3] = 2
        self._game.set_value(0, 3, 2)
        self.assertEqual(self._test_array, self._game.board)
        self.assertRaises(ValueError, self._game.set_value, 0, 0, 1)
        self.assertRaises(ValueError, self._game.set_value, 0, 0, -1)
        self.assertRaises(ValueError, self._game.set_value, 0, 0, 5)

    def test_move(self):
        self._test_array[3][0] = 2
        self._game.set_value(0, 0, 2)
        self._game.move('R')
        self.assertEqual(self._test_array, self._game.board)

        self._test_array[3][0] = 0
        self._test_array[3][3] = 4
        self._game.set_value(3, 2, 2)
        self._game.move('D')
        self.assertEqual(self._test_array, self._game.board)

        self._test_array[3][3] = 0
        self._test_array[0][3] = 4
        self._game.move('L')
        self.assertEqual(self._test_array, self._game.board)

        self._test_array[0][3] = 0
        self._test_array[0][0] = 8
        self._game.set_value(0, 0, 4)
        self._game.move('U')
        self.assertEqual(self._test_array, self._game.board)

    def test_empty_tiles(self):
        self.assertEqual(self._game.size ** 2, self._game.empty_tiles())

        for i in range((self._game.size ** 2) - 1):
            self._game.set_value(i // self._game.size, i % self._game.size, 2)
        self.assertEqual(1, self._game.empty_tiles())

        self._game.set_value(self._game.size-1, self._game.size-1, 2)
        self.assertEqual(0, self._game.empty_tiles())

    def test_game_finished(self):
        self.assertEqual(False, self._game.is_finished())

        for i in range((self._game.size ** 2)):
            self._game.set_value(i // self._game.size, i % self._game.size, 2)
        self.assertEqual(False, self._game.is_finished())

        for i in range((self._game.size ** 2)):
            self._game.set_value(i // self._game.size, i % self._game.size, 2 ** (i+1))
        self.assertEqual(True, self._game.is_finished())

    def test_grow_data(self):
        self._test_array[0][0] = 4
        self._game.set_value(0, 0, 2)
        self._game.grow_data(0, 0)
        self.assertEqual(self._test_array, self._game.board)

        self.assertRaises(ValueError, self._game.grow_data, 2, 2)

    def test_score(self):
        self.assertEqual(0, self._game.score)

        self._game.set_value(0, 0, 4)
        self.assertEqual(4, self._game.score)

        for i in range((self._game.size ** 2)):
            self._game.set_value(i // self._game.size, i % self._game.size, 2 if i % 2 == 0 else 4)
        self.assertEqual(3 * (self._game.size ** 2), self._game.score)


if __name__ == '__main__':
    unittest.main()
