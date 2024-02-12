from time import sleep
from src.pyt.GameManager import GameManager


def main():
    gm = GameManager(4)
    gm.init_game()
    gm.game_loop(verbose=True)


if __name__ == '__main__':
    main()
