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
import time
from car import Car
from board import Board
from breadth import Breadth
from depth import Depth
from rand import Random

def main():
	# check command lines arguments count
	if len(sys.argv) != 4:
		print("Not enough arguments:\n\tUsage: ./test.py  path/to/board  random/breadth/depth  number of tries")
		sys.exit(1)

	# defines how many times random should try to find a solution
	tries = int(sys.argv[3])
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
			board = setup_board(path)
			random = Random(board)
			random.solve()
			count +=1

	# solve using breadth first
	elif sys.argv[2] == "breadth":
		board = setup_board(path)
		breadth_class = Breadth(board)
		
		# start solving
		if detailed_benchmarking == True:
			cProfile.run('breadth_class.solve()')
		else:
			breadth_class.solve()

	# solve using depth first
	elif sys.argv[2] == "depth":
		board = setup_board(path)
		
		depth_class = Depth(board)
		
		# start solving
		if detailed_benchmarking == True:
			cProfile.run('depth_class.solve()')
		else:
			depth_class.solve()

	# invalid commandline arguments
	else:
		print("No valid algorithm:\n\tUsage: ./test.py  path/to/board  random/breadth/depth  number of tries")
		sys.exit(2)

	# print benchmark time
	t1 = time.time()
	print(t1 - t0)

# sets up a new board
def setup_board(path):
	# creating empty board class
	board = Board()
	# reads car possitions and dimmension from file and saves the info in board
	board.get_info(path)
	board.create_empty()
	board.setup()
	return board

# calls main
if __name__ == "__main__":
	main()