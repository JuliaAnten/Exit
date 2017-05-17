from board import Board
from queue import Queue
import copy
import sys

class Breadth(object):
	"""docstring for Solver"""

	def __init__(self, startboard):
		# root state of the board
		self.rootboard = startboard

		"""Breadth first specific"""
		# set up empty archive
		self.archive = {}
		# set up queue
		self.queue = Queue()
		# call solver() to start
		self.solve()

	def solve(self):
		print("solving...\nthis board:")
		print(self.rootboard)

		# add rootboard to archive with cars as key and 1 as value
		self.archive[hash(self.rootboard)] = 1

		# add rootboard to queue
		self.queue.put(self.rootboard)

		# while queue is not empty, keep looking
		while not self.queue.empty():

			# get board from queue
			current = self.queue.get()

			# if current is a winner
			if current.cars[0].x == self.rootboard.dimension - 2 :
				print("solved")
				print(current)
				print(current.solution_path)
				print(len(current.solution_path))

				exit(0)

			# for every car try to move it backwards or forwards
			for car in current.cars:
				# try forward
				self.try_move(current, car, 1)

				self.try_move(current, car, 0)

		print("not solved :(")


	def try_move(self, board, car, direction):
		# find a posibility
		possibility = self.move(board, car, direction)

		# if possibility is valid
		if possibility:
			# check if possibility is in archive
			if hash(possibility) not in self.archive:
				# add it to the list
				self.archive[hash(possibility)] = 1
				self.queue.put(possibility)


	def move(self, board, car, direction):
		"""Tries random moves on a car.
		   Returns a child board if move is valid, otherwise returns false."""
		outboard = copy.deepcopy(board)

		# vertical
		if car.orientation == "v":
			# if direction is forward
			if direction == 1:
				# one step forward
				# check if carmove goes out of bounds
				if car.y + car.length < outboard.dimension:
					if outboard.current_state[car.y + car.length][car.x] == "-":
						# valid move
						outboard.cars[outboard.cars.index(car)].y += 1
						outboard.update_current_state()
						# add move to solution_path
						outboard.solution_path.append(car.name + ", f")
						return outboard

			# if direction is backward
			else:
				# one step backward
				if car.y - 1 >= 0:
					if outboard.current_state[car.y - 1][car.x] == "-":
						# valid move
						outboard.cars[outboard.cars.index(car)].y -= 1
						outboard.update_current_state()
						# add move to solution_path
						outboard.solution_path.append(car.name + ", b")
						return outboard

		# if orientation is horizontal
		else:
			# if direction is forward
			if direction == 1:
				# one step forward
				if car.x + car.length < outboard.dimension:
					# check if there is room on the board to move
					if outboard.current_state[car.y][car.x + car.length] == "-":
						# valid move
						outboard.cars[outboard.cars.index(car)].x += 1
						outboard.update_current_state()
						# add move to solution_path
						outboard.solution_path.append(car.name + ", f")
						return outboard

			# if direction is backward
			else:
				# one step backward
				if car.x - 1 >= 0:
					# check if there is room on the board to move
					if outboard.current_state[car.y][car.x - 1] == "-":
						# valid move
						outboard.cars[outboard.cars.index(car)].x -= 1
						outboard.update_current_state()
						# add move to solution_path
						outboard.solution_path.append(car.name + ", b")
						return outboard

		# no valid moves
		return False
