###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
# 
# Defines Board class
#
###############################################

from car import Car


class Board(object):
	"""Defines the Board class"""

	def __init__(self):
		"""Initializes the dimension, car list,
		current state in a 2D array and a path to the solution.
		"""
		self.dimension = 0
		self.cars = []
		self.current_state = []
		self.solution_path = []

	def __repr__(self):
		"""Overrides standard repr method"""
		string = ""
		for row in self.current_state:
			string += str(row)
			string += "\n"
		return string
	
	def __hash__(self):
		"""Hashes the board using the hashes of cars in list. """
		a_hash = []
		[a_hash .append(str(hash(car))) for car in self.cars]
		return int("".join(a_hash))

	def __eq__(self, other):
		"""Overrides standard equals method"""
		return hash(self) == hash(other)
	
	def create_empty(self):
		"""Creates an empty 2D array to represent the current state of the board."""
		empty_board = [["-" for y in range(self.dimension)] for x in range(self.dimension)]
		self.current_state = empty_board
	
	def setup(self):
		"""Places the cars from the car list on the empty board"""

		for car in self.cars:

			# check what orientation the car is in (h = horizontal, v = vertical)
			if car.orientation == "h":
				for i in range(car.length):

					# check if a car doesn't go out of bounds
					if (car.x + i) >= self.dimension:
						print("car {}: x out of range: {}".format(car.name, (car.x + i)))
					elif car.y >= self.dimension:
						print("car {}: y out of range: {}".format(car.name, (car.y)))
					# place car on the board
					else:
						self.current_state[car.y][car.x + i] = car.name[0]

			elif car.orientation == "v":
				for i in range(car.length):

					if (car.y + i) >= self.dimension:
						print("car {}: y out of range: {}".format(car.name, (car.y + i)))
					elif car.x >= self.dimension:
						print("car {}: x out of range: {}".format(car.name, (car.x)))
					else:
						self.current_state[car.y + i][car.x] = car.name[0]

	def update_current_state(self):
		"""Updates current representation of board"""

		# creating a new empty board
		self.create_empty()

		# looking for car(s) locations
		for car in self.cars:

			# if the car orientation is h = horizontal
			if car.orientation == "h":
				for i in range(car.length):
					self.current_state[car.y][car.x + i] = car.name[0]

			# if car is v = vertical
			else:
				for i in range(car.length):
					self.current_state[car.y + i][car.x] = car.name[0]

	def get_info(self, file_path):
		"""Imports the information of the cars and populates car list"""

		# opening the input file and reading it
		file = open(file_path, "r")
		if file is None:
			print("Opening dictionary file failed")

		# parse input file line by line
		for line in file.readlines():

			# ignore irrelevant lines
			if not line.startswith("#") or line.startswith(" ") or line.startswith("\n"):

				# if line contains dimension info
				if line.startswith("dim:"):
					words = line.split()
					
					# set dimension
					self.dimension = int(words[1])

				# if line contains car info
				else:
					# split string
					words = line.split(',')

					# populate car object
					car = Car(words[0],
							int(words[1]),
							int(words[2]),
							int(words[3]),
							words[4])

					# append the car to the car list
					self.cars.append(car)

		file.close()
