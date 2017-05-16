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

		self.valid_count = 0

		# immediately start the solving, happens in test.py
		# self.solve()

	# returns true when the game is won
	def check_endstate(self):

		if self.current.cars[0].x == self.current.dimension - 2:
			return True

		i = self.current.cars[0].length
		while self.current.current_state[self.current.cars[0].y][self.current.cars[0].x + i] == "-":
			i+=1
			if self.current.cars[0].x + i == self.current.dimension:
				self.valid_count += i - 2
				return True

		return False

	def solve(self):
		#print("solving...")

		while (self.check_endstate() == False):
			# pick a random car from cars
			random_car = random.randint(0, len(self.current.cars) - 1)

			# generate random direction (1 is forward, 0 is backward)
			direction = random.randint(0,1)

			# try moving the random car
			self.move(self.current.cars[random_car],direction)

			# print current board
			# print(self.current)

			# update self.counter
			self.counter += 1

			#if self.counter % 100000 == 0:
			#	print("counter valid: {}".format(self.valid_count))

			#print("solved:\n in {} moves".format(self.counter))
			#print("Valid steps count: {}\n".format(self.valid_count))
		print("{}".format(self.valid_count))

	def move(self, car, direction):
		"""Tries random moves on a car."""

		# vertical
		if car.orientation == "v":
			# if direction is forward
			if direction == 1:
				# one step forward
				# check if carmove goes out of bounds
				if car.y + car.length < self.current.dimension:
					if self.current.current_state[car.y + car.length][car.x] == "-":
						# valid move
						self.valid_count += 1
						self.current.cars[self.current.cars.index(car)].y += 1
						self.solution.append(str(car.name + ", forward"))

			# if direction is backward
			else:
				# one step backward

				if car.y - 1 >= 0:
					if self.current.current_state[car.y - 1][car.x] == "-":
						# valid move
						self.valid_count += 1
						self.current.cars[self.current.cars.index(car)].y -= 1
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
						self.valid_count += 1
						self.current.cars[self.current.cars.index(car)].x += 1
						self.solution.append(str(car.name + ", forward"))

			# if direction is backward
			else:
				# one step backward
				if car.x - 1 >= 0:
					# self.current.current_state gets 2d array representation of board
					if self.current.current_state[car.y][car.x - 1] == "-":
						# valid move
						self.valid_count += 1
						self.current.cars[self.current.cars.index(car)].x -= 1
						self.solution.append(str(car.name + ", backward"))

		self.current.update_current_state()
