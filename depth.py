###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
#
# Defines how a Depth First Search is executed.
# 
###############################################


from board import Board
from queue import LifoQueue
import sys
import pickle
import mover
import validator


class Depth(object):
	"""Defines the Depth class"""

	def __init__(self, root_board):
		"""Depth always contains a root board, an archive and a queue"""

		# root state of the board
		self.board = root_board

		# set up empty archive
		self.archive = {}

		# set up a stack (i.e. queue with 'last in first out')
		self.stack = LifoQueue()

	def solve(self):
		"""Solves the root board using DFS"""

		# print the root board that the algorithm is trying to solve
		print("solving...\nthis board:")
		print(self.board)

		# add root board to archive
		self.archive[hash(self.board)] = 1

		# add root board to queue
		self.stack.put(self.board)

		# while queue is not empty, keep looking for a solution
		while not self.stack.empty():

			# get board from queue
			parent_board = self.stack.get()

			# if current board is a winner, stop looking
			if validator.check_endstate(parent_board):
				print("solved")
				print(parent_board)
				print(parent_board.solution_path)
				last_moves = validator.check_endstate(parent_board)
				print("Length of solution: {}".format(
					len(parent_board.solution_path) + last_moves))
				return

			# for every car try to move it
			for car in parent_board.cars:
				self.try_move(parent_board, car)

		# when the stack is empty the solotion is not found
		print("not solvable :(")

	def try_move(self, board, car):
		"""Tries moving a car forward, than backwards."""

		# set direction to backward
		direction = 0

		for i in range(2):
			# find a posibility
			child_board = mover.move(board, car, direction, True)

			# if possibility is valid
			if child_board:
				# check if possibility is in archive
				if hash(child_board) not in self.archive:
					# add it to archive and stack
					self.archive[hash(child_board)] = 1
					self.stack.put(child_board)

			# reverse direction
			direction = 1
