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

# check command lines arguments count
if len(sys.argv) != 3:
	print("Not enough arguments:\n\tUsage: ./test.py path/to/board random/breadth")
	sys.exit(1)


path = str(sys.argv[1])
# initialize board and set up the game 
board = Board(path)
board.setup_board()


# check given algorithm
if sys.argv[2] == "random":
	solver = Solver(board)
elif sys.argv[2] == "breadth":
	solver = Breadth(board)
else:
	print("No valid algorithm:\n\tUsage: ./test.py path/to/board random/breadth")
	sys.exit(2)



# print board
#print("\nStart board:")
#print(board)

# start the solving

print(solver.solve())

# # printing updated board
#print("\nEnd board:")
#print(solver.cars)
