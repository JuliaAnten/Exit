#!/usr/bin/env python3

###############################################
#
# this is the controller for the test.py game
#
# Usage: ./test.py path/to/board random/breadth
#
#
###############################################

import sys
from car import Car
from board import Board
from breadth import Breadth
from solver import Solver

path = "boards/03.txt"


# creating empty board class
board = Board()
# reads car possitions and dimmension from file and saves the info in board
board.get_info(path)
board.create_empty()
board.setup()
breadth_class = Breadth(board)
breadth_class.solve()