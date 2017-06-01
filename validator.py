###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
#
# Checks if a board has a winning configuration (i.e. has reached the endstate)
# 
###############################################

from board import Board


def check_endstate(board):
	"""Checks if a board has winning configuration."""

	# instantiate iterator to iterate over tiles between red car and exit
	i = board.cars[0].length
	
	# checks if tiles in front of car are empty
	while board.current_state[board.cars[0].y][board.cars[0].x + i] == "-":
		i += 1
		if board.cars[0].x + i == board.dimension:
			
			# return amount of free tiles between red car and exit
			return i - board.cars[0].length

	# if they aren't, return false
	return False
