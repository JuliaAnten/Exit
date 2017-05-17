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
import cProfile
from car import Car
from board import Board
from breadth import Breadth
from depth import Depth
from solver import Solver

# check command lines arguments count
if len(sys.argv) != 4:
	print("Not enough arguments:\n\tUsage: ./test.py  path/to/board  random/breadth/depth  number of tries")
	sys.exit(1)

tries = int(sys.argv[3])
path = str(sys.argv[1])

count = 1

# check given algorithm
if sys.argv[2] == "random":
	
	while count < tries:
		board = Board()
		# reads car possitions and dimmension from file and saves the info in board
		board.get_info(path)
		board.create_empty()
		board.setup()

		random = Solver(board)
		random.solve()
		count +=1
elif sys.argv[2] == "breadth":
	# creating empty board class
	board = Board()
	# reads car possitions and dimmension from file and saves the info in board
	board.get_info(path)
	board.create_empty()
	board.setup()
	breadth_class = Breadth(board)
	cProfile.run('breadth_class.solve()')
elif sys.argv[2] == "depth":
	# creating empty board class
	board = Board()
	# reads car possitions and dimmension from file and saves the info in board
	board.get_info(path)
	board.create_empty()
	board.setup()
	depth_class = Depth(board)
	cProfile.run('depth_class.solve()')
else:
	print("No valid algorithm:\n\tUsage: ./test.py  path/to/board  random/breadth/depth  number of tries")
	sys.exit(2)



# print board
#print("\nStart board:")
#print(board)

# start the solving



# # printing updated board
#print("\nEnd board:")
#print(solver.cars)
