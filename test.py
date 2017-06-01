#!/usr/bin/env python3

###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
# 
# This is the controller that binds all the code together
# 
# You can call one of three algorithms:
# - Breadth first search
# - Depth first search
# - Random search
#
# Boards can be found in /boards.
# 
# Usage: ./test.py path/to/board random/breadth/depth [amount of tries]
# 
###############################################

import sys
import time
from board import Board
from breadth import Breadth
from depth import Depth
from rand import Random


def main():
	"""Starts the program"""

	# check command lines argument count
	if len(sys.argv) < 3:
		print("Not enough arguments:\n\tUsage: ./test.py path/to/board"
			+ " random/breadth/depth [amount of tries]")
		sys.exit(1)

	# defines how many times a solution is searched for
	if len(sys.argv) == 4:
		tries = int(sys.argv[3])
	else:
		tries = 1
	
	# defines the path to the board that needs solving
	path = str(sys.argv[1])
	
	# counts how many solutions have been found already
	count = 0

	# get start time for basic benchmarking
	t0 = time.time()

	# solve using random search
	if sys.argv[2] == "random":
		while count < tries:

			# get current system time
			time0 = time.time()

			# sets up a start board from file
			board = setup_board(path)

			# creates a random instance
			random = Random(board)

			# starts the random algorithm to solve the puzzle
			random.solve()

			# count how many solutions have been found
			count += 1

	# solve using breadth first
	elif sys.argv[2] == "breadth":
		board = setup_board(path)
		breadth = Breadth(board)
		breadth.solve()

	# solve using depth first
	elif sys.argv[2] == "depth":
		board = setup_board(path)
		depth = Depth(board)
		depth.solve()

	# invalid commandline arguments
	else:
		print("Usage: ./test.py path/to/board random/breadth/depth"
			+ "[amount of tries]")
		sys.exit(2)

	# print benchmark time
	t1 = time.time()
	print("Total time: {}".format(t1 - t0))


def setup_board(path):
	"""Sets up a new board""" 
	board = Board()
	
	# reads car possitions and dimmension from file and saves the info in board
	board.get_info(path)
	
	board.create_empty()
	
	# places the cars from file on board 
	board.setup()

	return board

if __name__ == "__main__":
	main()
