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

		# immediately start the solving
		self.solve()

	def solve(self):
		print ("solving...")

		for car in (self.current.cars):
			self.move(car)


	def move(self, car):
		# vertical
		if car.orientation == "v":
			print("vertical---dowing nothign")
		# horizontal
		else:
			print("horizontal")
			# one step forward
			# self.current.current_state gets 2d array representation of board
			print()
			print(self.current.current_state[2][5])
			print()

			if self.current.current_state[car.x + car.length][car.y] == "-":
				print("valid")
				for auto in self.current.cars:
					print("for loop entered+")
					if auto.name == car.name:
						auto.x += 1
						print("x adjusted")
			else:
				print("invalid")
