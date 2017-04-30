from board import Board
import random

class Solver(object):
	"""docstring for Solver"""
	def __init__(self, startboard):
		# current state of the board
		self.current = startboard
		# winning state of board
		self.winstate = []
		# series of moves that solves the board
		self.solution = []
		# counter
		self.counter = 0

		# immediately start the solving
		self.solve()

	def solve(self):
		print("solving...")

		while (self.current.cars['red'].x != 4):
			# pick a random car from cars
			random_name = random.choice(list(self.current.cars.keys()))
			
			# try moving the random car
			self.move(self.current.cars[random_name])

			# print current board
			# print(self.current)

			# update self.counter
			self.counter += 1

		print("solved:\n in {} moves\n moves: {}".format(self.counter, self.solution))

	def move(self, car):
		"""Tries random moves on a car."""

		# generate random direction (1 is forward, 0 is backward)
		direction = random.randint(0,1)
		# print("hoi: {}".format(self.current.current_state[car.x][car.y - 1]))

		# vertical
		if car.orientation == "v":	
			# if direction is forward
			if direction == 1:
				# one step forward
				# check if carmove goes out of bounds
				if car.y + car.length < self.current.dimension:
					if self.current.current_state[car.y + car.length][car.x] == "-":
						# valid move
						self.current.cars[car.name].y += 1
						self.solution.append(str(car.name + ", forward"))
				
			# if direction is backward
			else:
				# one step backward
				
				if car.y - 1 > 0:
					if self.current.current_state[car.y - 1][car.x] == "-":
						# valid move
						self.current.cars[car.name].y -= 1
						self.solution.append(str(car.name + ", backward"))


		# if orientation is horizontal
		else:
			# if direction is forward			
			if direction == 1:					
				# one step forward
				if car.x + car.length < self.current.dimension:
					# self.current.current_state gets 2d array representation of board
					if self.current.current_state[car.y][car.x + car.length] == "-":
						# valid move
						self.current.cars[car.name].x += 1
						self.solution.append(str(car.name + ", forward"))
			
			# if direction is backward
			else:				
				# one step backward
				if car.x - 1 > 0:
					# self.current.current_state gets 2d array representation of board
					if self.current.current_state[car.y][car.x - 1] == "-":
						# valid move
						self.current.cars[car.name].x -= 1
						self.solution.append(str(car.name + ", backward"))

		self.current.update_current_state()

