###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
#
# Random board solver implementation. 
# 
#
###############################################

from board import Board
import random
import mover
import validator

class Random(object):
	"""docstring for Solver"""
	def __init__(self, startboard):
		# current state of the board
		self.current = startboard
		# winning state of board
		self.winstate = []
		# series of moves that solves the board
		self.solution = []
		# amount of moves needed to reach a state where red can move directly to exit
		self.valid_count = 0


	def solve(self):
		""" Start solving the board """
		while validator.check_endstate(self.current) == False:
			# pick a random car from cars
			random_car_index = random.randint(0, len(self.current.cars) - 1)
			random_car = self.current.cars[random_car_index]

			# generate random direction (1 is forward, 0 is backward)
			direction = random.randint(0,1)

			# try moving the random car
			new_board = mover.move(self.current, random_car,direction, False)
			if new_board:
				self.current = new_board
				self.current.update_current_state()
				self.valid_count += 1


		# print amount of moves needed to solve board
		print("{}".format(self.valid_count))

