###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
#
# Defines Breadth First Search
#
###############################################

from board import Board
from queue import Queue
import mover
import validator
import sys
import pickle
import time


class Breadth(object):	
	"""Defines the Breadth class"""

	def __init__(self, root_board):
		"""Breadth always contains a root board, an archive and a queue"""

		# root state of the board
		self.board = root_board

		# set up empty archive
		self.archive = {}
		
		# set up queue
		self.queue = Queue()
	
	def solve(self):
		"""Solves root board using BFS"""

		# print the root board the board that the the algorithm is trying to solve it
		print("solving...\nthis board: \n")
		print(self.board)

		# add rootboard to archive
		self.archive[hash(self.board)] = 1

		# add rootboard to queue
		self.queue.put(self.board)

		# while queue is not empty, keep looking for a solution
		while not self.queue.empty():

			# get board from queue
			parent_board = self.queue.get()

			# if the board is in a win possition, return the solution
			if validator.check_endstate(parent_board):
				print("solved")
				print(parent_board)
				print(parent_board.solution_path)
				last_moves = validator.check_endstate(parent_board)
				print("\nLength of solution: {}".format(
					len(parent_board.solution_path) + last_moves))
				return

			# for every car try to move it
			for car in parent_board.cars:
				self.try_move(parent_board, car)
				
		# when the queue is empty the solotion is not found
		print("not solved :(")

	def try_move(self, board, car):
		"""Tries moving a car forward, than backwards."""

		# set direction to backward
		direction = 0
		
		for i in range(2):
			# find a possibility
			child_board = mover.move(board, car, direction, True)

			# if possibility is valid
			if child_board:
				# check if possibility is in archive
				if hash(child_board) not in self.archive:
					# add board to archive and queue
					self.archive[hash(child_board)] = 1
					self.queue.put(child_board)

			# reverse direction
			direction = 1
