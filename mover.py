###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
#
# This class determines if a move is valid or not.
# If a move is valid it Returns a child board otherwise
# it returns false.
#
# Uses pickling instead of deepcopying. Argumentation for choice: 
# http://stackoverflow.com/questions/24756712/deepcopy-is-extremely-slow/29385667#29385667
###############################################


from board import Board
from car import Car
import pickle

"""
Checks in what orientation the car is in and in what direction its
has to move. than is select's the proper move funciton.
it returns a child board or false if the car could not move.
"""
def move(board, car, direction, pickle_on):

	# vertical forward
	if car.orientation == "v" and direction == 1:
		return vert_forward(board, car, direction, pickle_on)

	# vertical backward
	elif car.orientation == "v" and direction == 0:
		return vert_backward(board, car, direction, pickle_on)

	# horizontal forward
	elif car.orientation == "h" and direction == 1:
		return hor_forward(board, car, direction, pickle_on)

	# horizontal backward
	elif car.orientation == "h" and direction == 0:
		return hor_backward(board, car, direction, pickle_on)

	# no valid moves
	return False

"""Tries to move vertical forward.
If possible returns a child board.
else returns false."""
def vert_forward(board, car, direction, pickle_on):

	# check if a car doesnt move off the board
	if car.y + car.length < board.dimension:
		# check if the spot infront of the car is empty
		if board.current_state[car.y + car.length][car.x] == "-":

			if pickle_on == True:
				# creats a copy of the parent board
				child_board = pickle.loads(pickle.dumps(board, -1))
			else:
				child_board = board
                                
			# update's the location of the car only the coordinates
			child_board.cars[child_board.cars.index(car)].y += 1

			# update's the car locations on the board with the coordinates 
			child_board.update_current_state()

			# add move to solution_path
			child_board.solution_path.append(car.name + "↓")

			return child_board
	
	# returns if there are no valid moves
	return False

"""Tries to move vertical backward."""	
def vert_backward(board, car, direction, pickle_on):
	if car.y - 1 >= 0:
		if board.current_state[car.y - 1][car.x] == "-":
			if pickle_on == True:
				# creats a copy of the parent board
				child_board = pickle.loads(pickle.dumps(board, -1))
			else:
				child_board = board
                                
			child_board.cars[child_board.cars.index(car)].y -= 1
			child_board.update_current_state()
			child_board.solution_path.append(car.name + "↑")
			return child_board
	
	return False

"""Tries to move horizontal forward."""
def hor_forward(board, car, direction, pickle_on):
	if car.x + car.length < board.dimension:
		if board.current_state[car.y][car.x + car.length] == "-":
			if pickle_on == True:
				# creats a copy of the parent board
				child_board = pickle.loads(pickle.dumps(board, -1))
			else:
				child_board = board
                                
			child_board.cars[child_board.cars.index(car)].x += 1
			child_board.update_current_state()
			child_board.solution_path.append(car.name + "→")
			return child_board
	
	return False

"""Tries to move horizontal backward."""
def hor_backward(board, car, direction, pickle_on):
	if car.x - 1 >= 0:
		if board.current_state[car.y][car.x - 1] == "-":
			if pickle_on == True:
				# creats a copy of the parent board
				child_board = pickle.loads(pickle.dumps(board, -1))
			else:
				child_board = board
                    
			child_board.cars[child_board.cars.index(car)].x -= 1
			child_board.update_current_state()
			child_board.solution_path.append(car.name + "←")
			return child_board

	return False

