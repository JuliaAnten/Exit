from board import Board
from queue import Queue
import copy
import sys

class Breadth(object):
	"""docstring for Solver"""

	def __init__(self, startboard):
		# root state of the board
		self.rootboard = startboard
		# counter
		self.counter = 0

		"""Breadth first specific"""
		# set up empty archive
		self.archive = {}
		# set up queue (uses queue module)
		self.queue = Queue()

		# immediately start the solving
		# deze word nu geroepen in test.py
		self.solve()

	def solve(self):
		print("solving...")

		# add rootboard to archive with cars as key and 1 as value
		self.archive[hash(self.rootboard)] = 1

		# add rootboard to queue
		self.queue.put(self.rootboard)

		# while queue is not empty, keep looking
		print("while loop entering!")
		while (self.queue.empty() != True):

			# get first board from queue
			current = self.queue.get()
			print(current)

			# if current is a winner
			if current.cars[0].x == 4:
				print("solved!")
				print(current)
				print(current.solution_path)
				print(len(current.solution_path))
				# deze functie moeten we wat een passen
				# hij returned nu wel the board maar die vangen we nergens op.
				exit(0)
			# otherwise generate all possible boards adjecent to current
			# and add to board
			self.get_possibilities(current)
			print("queue length: " + str(self.queue.qsize()))
			self.counter += 1

		print("not solved :(")

		# print("solved:\n in {} moves\n moves: {}".format
		# 	(self.counter, self.solution))


	def get_possibilities(self, board):

		for car in board.cars:

			# try forward
			self.try_move(board, car, 1);

			# try backward
			self.try_move(board, car, 0);


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

	def try_move(self, board, car, direction):
		# find a posibility
		possibility = self.move(board, car, direction)

		# if possibility is valid
		if possibility != False:

			# check if possibility is in archive
			if hash(possibility) not in self.archive:
				# add it to the list
				self.archive[hash(possibility)] = 1
				self.queue.put(possibility)
				# # print("forward")
				# print(board.cars)
				# print(possibility)
