from board import Board
from queue import Queue
import copy
import sys

class Breadth(object):
	"""docstring for Solver"""

	def __init__(self, startboard):
		# root state of the board
		self.rootboard = startboard
		# series of moves that solves the board
		self.solution = []
		# counter
		self.counter = 0

		"""Breadth first specific"""
		# set up empty archive
		self.archive = {}
		# set up queue (uses queue module)
		self.queue = Queue()

		# # immediately start the solving
		# # deze word nu geroepen in test.py
		# self.solve()

	def solve(self):
		print("solving...")

		print(self.rootboard.cars)

		self.archive[hash(self.rootboard)] = 1
		self.queue.put(self.rootboard)

		print("while loop entering!")
		while (self.queue.empty() != True):

			# get first board from queue
			current = self.queue.get()

			# print(current.cars['red'].x)
			# print(current)
			# if current is a winner
			if current.cars['red'].x == 4:
				print("solved!")

				# deze functie moeten we wat een passen
				# hij returned nu wel the board maar die vangen we nergens op.
				return current

			# otherwise generate all possible boards adjecent to current
			self.get_possibilities(current)

		# print("solved:\n in {} moves\n moves: {}".format
		# 	(self.counter, self.solution))


	def get_possibilities(self, board):

		for name, car in board.cars.items():

			# if forward is valid
			possibility = self.move(board, car, 1)
			if possibility != False:

				# check if possibility is in archive
				if hash(possibility) not in self.archive:
						# board is in archive dus niet toevoegend
					# board is niet in archive
					# add it to the list
					self.archive[hash(possibility)] = 1
					self.queue.put(possibility)

			# if backward is valid
			possibility = self.move(board, car, 0)
			if possibility != False:

				# check if possibility is in archive
				if hash(possibility) not in self.archive:
						# board is in archive dus niet toevoegend
					# board is niet in archive
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
						outboard.cars[car.name].y += 1
						outboard.update_current_state()
						return outboard

			# if direction is backward
			else:
				# one step backward
				if car.y - 1 >= 0:
					if outboard.current_state[car.y - 1][car.x] == "-":
						# valid move
						outboard.cars[car.name].y -= 1
						outboard.update_current_state()
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
						outboard.cars[car.name].x += 1
						outboard.update_current_state()
						return outboard

			# if direction is backward
			else:
				# one step backward
				if car.x - 1 >= 0:
					# check if there is room on the board to move
					if outboard.current_state[car.y][car.x - 1] == "-":
						# valid move
						outboard.cars[car.name].x -= 1
						outboard.update_current_state()
						return outboard

		# no valid moves
		return False
