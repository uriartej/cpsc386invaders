#!/usr/bin/env python3
# Juan Uriarte
# uriarte.juan@csu.fullerton.edu
# uriartej

"""
Imports the the game demo and executes the main function.
"""

from videogame.game import MyVideoGame

def main():
    game = MyVideoGame()
    game.run()

if __name__ == "__main__":
    main()
