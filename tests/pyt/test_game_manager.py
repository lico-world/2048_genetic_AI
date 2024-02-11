import unittest
from src.pyt.GameManager import GameManager


class TestGameManager(unittest.TestCase):
    def setUp(self):
        self._game_manager = GameManager(4, False)
        self._test_array = [[0 for _ in range(4)] for _ in range(4)]

    def test_init(self):
        self._test_array[3][3] = 2
        self._game_manager.init_game()
        self.assertEqual(self._test_array, self._game_manager.game.board)
        self.assertEqual(2, self._game_manager.game.score)

    def test_end_game(self):
        self._game_manager.game_loop('ULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUL')
        self.assertEqual(144, self._game_manager.game.score)

    def test_game_loop(self):
        self._game_manager.game_loop('ULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULULUL')
        self._test_array = [[64, 4, 16, 4], [32, 8, 4, 2], [4, 0, 0, 0], [4, 2, 0, 0]]
        self.assertEqual(self._test_array, self._game_manager.game.board)


if __name__ == '__main__':
    unittest.main()