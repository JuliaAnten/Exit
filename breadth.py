###############################################
# 
# Code written by: 
# - Julia Anten
# - Sander Swierts 
# - Maxim Stomphorst
#
# This is our emplementation of a breadth first search BFS.
# 
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
			
	"""Contains the Board class that contains the Car class.
	A BFS need a archive to check if a board is already made and it need a Queue
	to pick the next board from too search."""
	def __init__(self, root_board):
		# root state of the board
		self.board = root_board

		# set up empty archive
		self.archive = {}
		
		# set up queue
		self.queue = Queue()


	"""The BFS algorithm.
	Input is a Board class.
	Output no output is return.
	It prints the solution and the solved board."""
	def solve(self):

		# print the root board the board that the the algorithm is trying to solve it
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

			# if the board is in a win possition
			if validator.check_endstate(parent_board):
				print("solved")
				print(parent_board)
				print(parent_board.solution_path)
				print(len(parent_board.solution_path))
				return

			# for every car try to move it backwards and forwards
			for car in parent_board.cars:
                
				self.try_move(parent_board, car)
				
		# when the queue is empty the solotion is not found
		print("not solved :(")


	"""Tries moving a car forward than backwards."""
	def try_move(self, board, car):

		# move car forward
		direction = 0
		
		for i in range(2):
			# find a posibility
			child_board = mover.move(board, car, direction)

			# if possibility is valid
			if child_board:
				# check if possibility is in archive
				if hash(child_board) not in self.archive:
					# add board to archive
					self.archive[hash(child_board)] = 1
					# add the board to the queue
					self.queue.put(child_board)

			# reverse direction try to move car backwards
			direction = 1