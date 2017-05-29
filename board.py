###############################################
# 
# Code written by: 
# - Julia Anten
# - Sander Swierts 
# - Maxim Stomphorst
# 
# This call creats a rush hour board class with its components.
#
###############################################

from car import Car

class Board(object):

	"""docstring for Board"""
	def __init__(self):
        # dimensions of the board
		self.dimension = ()
        # list of car objects
		self.cars = []
        # the board status
		self.current_state = []
        # path to solution when a new child is created it appends the move
		self.solution_path = []

	def __repr__(self):
		string = ""
		for row in self.current_state:
			string+=str(row)
			string+="\n"
		return string


	"""If hash is called's on board it hashs the board
	by all the cars that are on the board.
	name, x position, and y position this done in the car class.
	a hash has to return a interger that way the code converts a string."""	
	def __hash__(self):
		a_hash = []
		[a_hash .append(str(hash(car))) for car in self.cars]
		return int("".join(a_hash))

	"""If a equality test is called on the class 
	this determines how it is handelt."""
	def __eq__(self, other):
		return hash(self) == hash(other)

	"""Creates a empty doubly linked list,
	a representation of the rush hour board."""
	def create_empty(self):
		empty_board = [["-" for y in range(self.dimension)] for x in range(self.dimension)]
		self.current_state = empty_board

	"""Places the cars from the car class on the empty board"""
	def setup(self):

		# selects every car one by one
		for car in self.cars:

			# check what orientation the car is in (h = horizontal)
			if car.orientation == "h":
				for i in range(car.length):

					# check if a car doesn't go out of bounds
					if (car.x + i) >= self.dimension:
						print("car {}: x out of range: {}".format(car.name, (car.x +i)))
					elif car.y >= self.dimension:
						print("car {}: y out of range: {}".format(car.name, (car.y)))
					# place car on the board
					else:
						self.current_state[car.y][car.x + i] = car.name[0]

			# v = verital
			if car.orientation == "v":
				for i in range(car.length):

					if (car.y + i) >= self.dimension:
						print("car {}: y out of range: {}".format(car.name, (car.y+i)))
					elif car.x >= self.dimension:
						print("car {}: x out of range: {}".format(car.name, (car.x)))
					else:
						self.current_state[car.y + i][car.x] = car.name[0]

	""" """
	def update_current_state(self):

		# creating a new empty board
		self.create_empty()

		# looking for car(s) locations
		for car in self.cars:

			# if the car orientation is h = horizontal
			if car.orientation == "h":
				for i in range(car.length):
					# placeing the car on the board (if updatede)
					self.current_state[car.y][car.x + i] = car.name[0]

			# if the are is v = verital
			else:
				for i in range(car.length):
					self.current_state[car.y + i][car.x] = car.name[0]

		return True

	"""Imports the car locations from a file stroing the information in as as list 
	in self.cars."""
	def get_info(self, file_path):
		# opening the input file and reading it
		file = open(file_path, "r")
		if file == None:
			print("Opening dictionary file failed")

		# parse input file line by line
		for line in file.readlines():

			# ignore irrelevant lines
			if not line.startswith("#") or line.startswith(" ") or line.startswith("\n"):

				# if line contains dimension info
				if line.startswith("dim:"):

					words = line.split()
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

					# append the car to the car dictionary
					self.cars.append(car)

		file.close()
