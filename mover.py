from board import Board
from car import Car
import pickle

"""
Tries moves for a car. Returns a child board if move is valid,
otherwise returns false.

Uses pickling instead of deepcopying. Argumentation for choice: 
http://stackoverflow.com/questions/24756712/deepcopy-is-extremely-slow/29385667#29385667
"""

def move(board, car, direction):
	# vertical forward
	if car.orientation == "v" and direction == 1:
		return vert_forward(board, car, direction)

	# vertical backward
	elif car.orientation == "v" and direction == 0:
		return vert_backward(board, car, direction)

	# horizontal forward
	elif car.orientation == "h" and direction == 1:
		return hor_forward(board, car, direction)

	# horizontal backward
	elif car.orientation == "h" and direction == 0:
		return hor_backward(board, car, direction)

	# no valid moves
	return False

# tries to move vertical forward
def vert_forward(board, car, direction):
	if car.y + car.length < board.dimension:
		if board.current_state[car.y + car.length][car.x] == "-":
			child_board = pickle.loads(pickle.dumps(board, -1))
			# valid move
			child_board.cars[child_board.cars.index(car)].y += 1
			child_board.update_current_state()
			# add move to solution_path
			child_board.solution_path.append(car.name + "↑")
			return child_board
	
	# returns if there are no valid moves
	return False

# tries to move vertical backward		
def vert_backward(board, car, direction):
	if car.y - 1 >= 0:
		if board.current_state[car.y - 1][car.x] == "-":
			child_board = pickle.loads(pickle.dumps(board, -1))
			# valid move
			child_board.cars[child_board.cars.index(car)].y -= 1
			child_board.update_current_state()
			# add move to solution_path
			child_board.solution_path.append(car.name + "↓")
			return child_board
	
	# returns if there are no valid moves
	return False

# tries to move horizontal forward
def hor_forward(board, car, direction):
	if car.x + car.length < board.dimension:
		# check if there is room on the board to move
		if board.current_state[car.y][car.x + car.length] == "-":
			child_board = pickle.loads(pickle.dumps(board, -1))
			# valid move
			child_board.cars[child_board.cars.index(car)].x += 1
			child_board.update_current_state()
			# add move to solution_path
			child_board.solution_path.append(car.name + "→")
			return child_board
	
	# returns if there are no valid moves
	return False

# tries to move horizontal backward
def hor_backward(board, car, direction):
	if car.x - 1 >= 0:
		# check if there is room on the board to move
		if board.current_state[car.y][car.x - 1] == "-":
			child_board = pickle.loads(pickle.dumps(board, -1))
			# valid move
			child_board.cars[child_board.cars.index(car)].x -= 1
			child_board.update_current_state()
			# add move to solution_path
			child_board.solution_path.append(car.name + "←")
			return child_board

	# returns if there are no valid moves
	return False

