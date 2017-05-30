###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
#
# This Check if a board is in s solved position. 
# 
###############################################

from board import Board

"""Check if a board is in the win position
if so it returns true else false """
def check_endstate(board):
	i = board.cars[0].length
	
	# checks if tiles in front of car are empty
	while board.current_state[board.cars[0].y][board.cars[0].x + i] == "-":
		i+=1
		if board.cars[0].x + i == board.dimension:
			return True

	# if they aren't, return false
	return False
