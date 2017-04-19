from board import Board

class Solver(object):
	"""docstring for Solver"""
	def __init__(self, startboard):
		# current state of the board
		self.current = startboard
		# winning state of board
		self.winstate = []
		# series of moves that solves the board
		self.solution = []

		# archive
		self.archive = []

		# queue
		self.queue = []

		# immediately start the solving
		self.solve()

	def solve(self):
		print ("hello, this is solver speaking")

		print(self.current.dimension)

		