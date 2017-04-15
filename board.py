from car import Car

class Board(object):
	"""docstring for Board"""
	def __init__(self, path):
		self.path = path
		self.dimension = 0
		self.cars = []
		self.current_state = []
		self.setup_board()

	
	# initialize empty board
	def make(self):
		state = [["-" for y in range(self.dimension)] for x in range(self.dimension)]
		self.current_state = state
		print("empty board created")

	
	# initialize board with cars on it
	def setup_board(self):

		# import start configuration from file
		self.import_board(self.path)

		# create empty board
		self.make()

		# initalize cars
		print("List of cars:")
		for car in self.cars:
			print(car.name, car.x, car.y, car.length, car.orientation)
			
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

		print("\n")
		print("Cars have been put onto the board")

	
	# import board configuration and store contents accordingly
	def import_board(self, path):
		# opening the input file and reading it
		file = open(path, "r")
		if file == None:
			print("Opening dictionary file fialed")

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
					words = line.split(',')

					# create dictionary 
					dic = {'name': words[0], 'x': int(words[1]), 'y': int(words[2]), 'length': int(words[3]), 'orientation': words[4]}

					# # extracting individuel words and putting them in a dict
					# dic["name"] = words[0]
					# dic["x"] = words[1]
					# dic["y"] = words[2]
					# dic["length"] = words[3]
					# dic["orientation"] = words[4]

					car = Car(dic['name'],
							  dic['x'], 
							  dic["y"],
							  dic["length"],
							  dic["orientation"])


					self.cars.append(car)
		file.close()
		print("input file processed")
		