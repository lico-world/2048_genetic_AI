from time import sleep
from src.pyt.Game import *


def main():
    game = Game(4)
    game.set_value(2, 1, 2)
    print(game)

    sleep(1)
    game.move('R')
    game.set_value(3, 0, 2)
    print(game)

    sleep(1)
    game.move('U')
    game.set_value(3, 2, 2)
    print(game)


if __name__ == '__main__':
    main()
