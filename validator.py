from board import Board

# returns true when tiles in front of car is empty
def check_endstate(board):
	i = board.cars[0].length
	
	# checks if tiles in front of car are empty
	while board.current_state[board.cars[0].y][board.cars[0].x + i] == "-":
		i+=1
		if board.cars[0].x + i == board.dimension:
			return True

	# if they aren't, return false
	return False
