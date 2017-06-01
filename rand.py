###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
#
# Defines how a Random Search is executed
# 
#
###############################################

from board import Board
import random
import mover
import validator


class Random(object):
	"""Defines Random class"""
	
	def __init__(self, startboard):
		"""Random always contains a current board (starting with a given board, and
		the amount of valid moves made thus far.
		"""

		# current state of the board
		self.current = startboard
		# amount of moves needed to reach a state where red can move directly to exit
		self.valid_count = 0

	def solve(self):
		"""Starts solving the board"""
		
		# keep looking until endstate is reached.
		while validator.check_endstate(self.current) is False:
			
			# pick a random car from cars
			random_car_index = random.randint(0, len(self.current.cars) - 1)
			random_car = self.current.cars[random_car_index]

			# generate random direction (1 is forward, 0 is backward)
			direction = random.randint(0, 1)

			# try moving the random car
			new_board = mover.move(self.current, random_car, direction, False)
			if new_board:
				
				# if a valid move is found, replace old board with new board
				self.current = new_board
				self.current.update_current_state()
				self.valid_count += 1

		# add free tiles in front of red car to the count of moves
		self.valid_count += validator.check_endstate(self.current)

		# print amount of moves needed to solve board
		print("\nLength of solution: {}".format(self.valid_count))
