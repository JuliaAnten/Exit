from car import Car

class Board(object):
	"""docstring for Board"""
	def __init__(self):
		self.dimension = 0
		self.cars = []
		self.current_state = []
		self.solution_path = []

	def __repr__(self):
		string = ""
		for row in self.current_state:
			string+=str(row)
			string+="\n"
		return string

	def __hash__(self):
		lst = []
		"""hash() has to return an integer.
		This is our solution, but there has to be a better way"""
		[lst.append(str(hash(car))) for car in self.cars]
		return int("".join(lst))

	def __eq__(self, other):
		return hash(self) == hash(other)

	# initialize empty board
	def make(self):
		state = [["-" for y in range(self.dimension)] for x in range(self.dimension)]
		self.current_state = state

	# initialize board with cars on it
	def setup_board(self, path):

		# import start configuration from file
		self.import_board(path)

		# create empty board
		self.make()

		# initalize cars
		for car in self.cars:
			if car.orientation == "h":
				for i in range(car.length):
					if (car.x + i) >= self.dimension:
						print("car {}: x out of range: {}".format(car.name, (car.x+i)))
					elif car.y >= self.dimension:
						print("car {}: y out of range: {}".format(car.name, (car.y)))
					else:
						self.current_state[car.y][car.x + i] = car.name[0]


			if car.orientation == "v":
				for i in range(car.length):
					if (car.y + i) >= self.dimension:
						print("car {}: y out of range: {}".format(car.name, (car.y+i)))
					elif car.x >= self.dimension:
						print("car {}: x out of range: {}".format(car.name, (car.x)))
					else:
						self.current_state[car.y + i][car.x] = car.name[0]

	def update_current_state(self):

		# creating a new empty board
		self.make()

		# looking for car(s) locations
		for car in self.cars:
			# print all the cars that exsist
			# print(car.name, "\t", car.x, car.y, car.length, car.orientation)

			# if the car orientation is h = horizontal
			if car.orientation == "h":
				for i in range(car.length):
					# placeing the car on the board (if updatede)
					# the updatede location
					self.current_state[car.y][car.x + i] = car.name[0]

			# if the are is v = verital
			else:
				for i in range(car.length):
					self.current_state[car.y + i][car.x] = car.name[0]

		return True

	# import board configuration and store contents accordingly
	def import_board(self, file_path):
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
