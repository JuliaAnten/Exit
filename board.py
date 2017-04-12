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
		