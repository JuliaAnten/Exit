#!/usr/bin/env python3

###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
# 
# This is the controller for how a board is solved.
# 
# You can call one of three algorithms:
# - Breadth first search
# - Depth first search
# - Random
# 
# Usage: ./test.py path/to/board random/breadth/depth [amount of tries]
# 
#
###############################################

import sys
import time
from board import Board
from breadth import Breadth
from depth import Depth
from rand import Random


def main():

	# check command lines arguments count
	if len(sys.argv) != 3:
		print("Not enough arguments:\n\tUsage: ./test.py path/to/board random/breadth/depth [amount of tries]")
		sys.exit(1)

	# defines how many times a solution is searched for
	if len(sys.argv) == 4:
		tries = int(sys.argv[3])
	else:
		tries = 1
	
	# defines the path to the board that needs solving
	path = str(sys.argv[1])
	
	# counts how many solutions have been found by random
	count = 0

	# set to true to get detailed benchmarking info
	detailed_benchmarking = False

	# for benchmarking since cProfile slows everything down
	t0 = time.time()

	# check given algorithm
	if sys.argv[2] == "random":
		while count < tries:

			# get current system time
			time0 = time.time()

			# creates a loaded board class
			board = setup_board(path)

			# creates a random class
			random = Random(board)

			# starts the random algorithm to solve the puzzle
			random.solve()

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
		print("Usage: ./test.py path/to/board random/breadth/depth [amount of tries]")
		sys.exit(2)

	# print benchmark time
	t1 = time.time()
	print("Total time:")
	print(t1 - t0)

"""sets up a new board""" 
def setup_board(path):
	# creating empty board class
	board = Board()
	# reads car possitions and dimmension from file and saves the info in board
	board.get_info(path)
	# creats a empty board
	board.create_empty()
	# places the car's from the file on the just created empty board. 
	board.setup()

	# returns a filled board class ready for any solve methode
	return board

if __name__ == "__main__":
	main()