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

if not 1 < len(sys.argv) < 3:
	print("Usage: ./test.py path/to/board")

else:
	path = str(sys.argv[1])
	# initialize board and set up the game
	board = Board(path)
	board.setup_board()
	
	# print board
	for row in board.current_state:
		print(row)

	# start the solving
	solver = Solver(board)	
