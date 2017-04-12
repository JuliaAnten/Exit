class Board(object):
	"""docstring for Board"""
	def __init__(self, dimension, cars=None):
		self.dimension = dimension
		self.cars = cars
		self.state = []

	def make(self):
		state = [["-" for y in range(self.dimension)] for x in range(self.dimension)]
		self.state = state

		