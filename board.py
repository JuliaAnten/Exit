from car import Car

class Board(object):
	"""docstring for Board"""
	def __init__(self, dimension, cars=None):
		self.dimension = dimension
		self.cars = cars
		self.state = []

	def make(self):
		state = [["-" for y in range(self.dimension)] for x in range(self.dimension)]
		self.state = state

	def init_cars(self, input_cars):
		# create empty board
		self.make()

		#initiliaze list of Car objects
		cars = []

		# initalize cars
		for car in input_cars:
			c = Car(car["name"], car["x"], car["y"], car["length"], car["orientation"])
			cars.append(c)
			
			if c.orientation == "h":
				for i in range(c.length):
					self.state[c.y][c.x + i] = c.name[0]

			if c.orientation == "v":
				for i in range(c.length):
					self.state[c.y + i][c.x] = c.name[0]

	def import_board(self, path):
		lst =  []

		# opening the board.txt file and reading it
		file = open(path, "r")
		if file == None:
			print("Opening dictionary file fialed")


		for line in file.readlines(): 
			if not line.startswith("#") or line.startswith(" ") or line.startswith("\n"):

				if line.startswith("dim:"):

					words = line.split()
					dim = words[1]

				else:
					words = line.split(',')

					# create dictionary 
					dic = {}

					# exstracting individuel words and putting them in a dict
					dic["name"] = words[0]
					dic["x"] = words[1]
					dic["y"] = words[2]
					dic["length"] = words[3]
					dic["orientation"] = words[4]

					lst.append(dic)

		file.close()

		return dim,lst
		