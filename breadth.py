from board import Board
from queue import Queue
import mover
import validator
import sys
import pickle
import time

class Breadth(object):
	"""docstring for Breadth"""
			

	def __init__(self, root_board):
		# root state of the board
		self.board = root_board

		# set up empty archive
		self.archive = {}
		
		# set up queue
		self.queue = Queue()

	def solve(self):
		print("solving...\nthis board: \n")
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
			if validator.check_endstate(parent_board):
				print("solved")
				print(parent_board)
				print(parent_board.solution_path)
				print(len(parent_board.solution_path))
				return

			# for every car try to move it backwards or forwards
			for car in parent_board.cars:
                
				# try forward and backward
				self.try_move(parent_board, car)

		print("not solved :(")


	# tries moving forward and backward
	def try_move(self, board, car):
		direction = 0
		
		for i in range(2):
			# find a posibility
			child_board = mover.move(board, car, direction)

			# if possibility is valid
			if child_board:
				# check if possibility is in archive
				if hash(child_board) not in self.archive:
					# add it to the list
					self.archive[hash(child_board)] = 1
					self.queue.put(child_board)

			# reverse direction
			direction = 1