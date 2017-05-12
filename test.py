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
if len(sys.argv) != 4:
	print("Not enough arguments:\n\tUsage: ./test.py  path/to/board  random/breadth  number of tries")
	sys.exit(1)

tries = int(sys.argv[3])
path = str(sys.argv[1])
# initialize board and set up the game 
board = Board(path)
board.setup_board()


solver = Solver(board)
solver.solve()

count = 1

# check given algorithm
if sys.argv[2] == "random":
	
	while count < tries:
		board = Board(path)
		board.setup_board()
		solver = Solver(board)
		solver.solve()
		count +=1
elif sys.argv[2] == "breadth":
	while count < tries:
		board = Board(path)
		board.setup_board()
		solver = Breadth(board)
		solver.solve()
		count +=1
else:
	print("No valid algorithm:\n\tUsage: ./test.py  path/to/board  random/breadth  number of tries")
	sys.exit(2)



# print board
#print("\nStart board:")
#print(board)

# start the solving



# # printing updated board
#print("\nEnd board:")
#print(solver.cars)
