from board import Board
from queue import LifoQueue
import copy
import sys
import pickle

class Depth(object):
	"""docstring for Solver"""

	def __init__(self, root_board):
		# root state of the board
		self.board = root_board

		"""Depth first specific"""
		# set up empty archive
		self.archive = {}
		# set up queue
		self.queue = LifoQueue()

	def solve(self):
		print("solving...\nthis board:")
		print(self.board)

		# add rootboard to archive with cars as key and 1 as value
		self.archive[hash(self.board)] = 1

		# add rootboard to queue
		self.queue.put(self.board)

		# while queue is not empty, keep looking
		while not self.queue.empty():

			# get board from queue
			parent_board = self.queue.get()

			# if current is a winner
			if parent_board.cars[0].x == self.board.dimension - 2 :
				print("solved")
				print(parent_board)
				print(parent_board.solution_path)
				print(len(parent_board.solution_path))
				return

			# for every car try to move it backwards or forwards
			for car in parent_board.cars:
                
				# try forward
				self.try_move(parent_board, car, 1)

				self.try_move(parent_board, car, 0)

		print("not solved :(")


	def try_move(self, board, car, direction):
		# find a posibility
		child_board = self.move(board, car, direction)

		# if possibility is valid
		if child_board:
			# check if possibility is in archive
			if hash(child_board) not in self.archive:
				# add it to the list
				self.archive[hash(child_board)] = 1
				self.queue.put(child_board)


	def move(self, board, car, direction):
		"""
		Tries random moves on a car. Returns a child board if move is valid,
		otherwise returns false.

		Uses pickling instead of deepcopying. Argumentation for choice: 
		http://stackoverflow.com/questions/24756712/deepcopy-is-extremely-slow/29385667#29385667
		"""

		# vertical
		if car.orientation == "v":
			# if direction is forward
			if direction == 1:
				# one step forward
				# check if carmove goes out of bounds
				if car.y + car.length < board.dimension:
					if board.current_state[car.y + car.length][car.x] == "-":
						child_board = pickle.loads(pickle.dumps(board, -1))
						# valid move
						child_board.cars[child_board.cars.index(car)].y += 1
						child_board.update_current_state()
						# add move to solution_path
						child_board.solution_path.append(car.name + ", ↑")
						return child_board

			# if direction is backward
			else:
				# one step backward
				if car.y - 1 >= 0:
					if board.current_state[car.y - 1][car.x] == "-":
						child_board = pickle.loads(pickle.dumps(board, -1))
						# valid move
						child_board.cars[child_board.cars.index(car)].y -= 1
						child_board.update_current_state()
						# add move to solution_path
						child_board.solution_path.append(car.name + ", ↓")
						return child_board

		# if orientation is horizontal
		else:
			# if direction is forward
			if direction == 1:
				# one step forward
				if car.x + car.length < board.dimension:
					# check if there is room on the board to move
					if board.current_state[car.y][car.x + car.length] == "-":
						child_board = pickle.loads(pickle.dumps(board, -1))
						# valid move
						child_board.cars[child_board.cars.index(car)].x += 1
						child_board.update_current_state()
						# add move to solution_path
						child_board.solution_path.append(car.name + ", →")
						return child_board

			# if direction is backward
			else:
				# one step backward
				if car.x - 1 >= 0:
					# check if there is room on the board to move
					if board.current_state[car.y][car.x - 1] == "-":
						child_board = pickle.loads(pickle.dumps(board, -1))
						# valid move
						child_board.cars[child_board.cars.index(car)].x -= 1
						child_board.update_current_state()
						# add move to solution_path
						child_board.solution_path.append(car.name + ", ←")
						return child_board

		# no valid moves
		return False
