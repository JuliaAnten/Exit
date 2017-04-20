#!/usr/bin/env python3

###############################################
#
# this is the controller for the test.py game
#
# Usage: ./test.py path/to/board
#
#
###############################################

import sys
from car import Car
from board import Board
from solver import Solver


assert (1 < len(sys.argv) < 3),	"Usage: ./test.py path/to/board"

path = str(sys.argv[1])
# initialize board and set up the game
board = Board(path)
board.setup_board()

# print board
board.print()

# start the solving
solver = Solver(board)

board.update_current_state()

# printing updated board
board.print()