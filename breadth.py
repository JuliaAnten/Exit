from board import Board
from queue import Queue

class Breadth(object):
	"""docstring for Solver"""

	def __init__(self, startboard):
		# root state of the board
		self.rootboard = startboard
		# series of moves that solves the board
		self.solution = []
		# counter
		self.counter = 0

		"""Breadth first specific"""		
		# set up empty archive
		self.archive = []
		# set up queue (uses queue module)
		self.queue = Queue(0)

		# immediately start the solving
		self.solve()

	def solve(self):
		print("solving...")

		self.archive.append(self.rootboard)
		self.queue.put(self.rootboard)

		while (self.queue.empty() != True):
			print("while loop entered")
			
			# get first board from queue
			current = self.queue.get()

			# if current is a winner
			if current.cars['red'].x == 4:
				print("solved!")
				return current

			# otherwise generate all possible boards adjecent to current
			possibilities = self.get_possibilities(current)
			print("\npossibilities:")
			for i in possibilities:
				
				print(i)
			print("/possibilities")

			# check for possible boards if they're in the archive
			# for board in possibilities:
			# 	if board is not in self.archive:
			# 		self.archive.append(board)
			# 		board.parent = current
			# 		queue.put(board)

		print("solved:\n in {} moves\n moves: {}".format
			(self.counter, self.solution))

	
	def get_possibilities(self, board):
		lst = []
		for name, car in board.cars.items():

			print(car)
			# if forward is valid
			possibility = self.move(board, car, 1)
			if possibility != False:
				# add it to the list
				lst.append(possibility)
				print("forward")
				print(board.cars)
				print(possibility)

			
			# if backward is valid
			possibility = self.move(board, car, 0)
			if possibility != False:
				# add it to the list
				lst.append(possibility)
				print("backward")
				print(board.cars)
				print(possibility)

		return lst

	def move(self, board, car, direction):
		"""Tries random moves on a car. 
		   Returns a child board if move is valid, otherwise returns false."""
		outboard = board.deepcopy()

		# vertical
		if car.orientation == "v":	
			# if direction is forward
			if direction == 1:
				# one step forward
				# check if carmove goes out of bounds
				if car.y + car.length < outboard.dimension:
					if outboard.current_state[car.y + car.length][car.x] == "-":
						# valid move
						outboard.cars[car.name].y += 1
						outboard.update_current_state()
						return outboard
				
			# if direction is backward
			else:
				# one step backward
				if car.y - 1 > 0:
					if outboard.current_state[car.y - 1][car.x] == "-":
						# valid move
						outboard.cars[car.name].y -= 1
						outboard.update_current_state()
						return outboard

		# if orientation is horizontal
		else:
			# if direction is forward			
			if direction == 1:					
				# one step forward
				if car.x + car.length < outboard.dimension:
					# check if there is room on the board to move
					if outboard.current_state[car.y][car.x + car.length] == "-":
						# valid move
						outboard.cars[car.name].x += 1
						outboard.update_current_state()
						return outboard
			
			# if direction is backward
			else:				
				# one step backward
				if car.x - 1 > 0:
					# check if there is room on the board to move
					if outboard.current_state[car.y][car.x - 1] == "-":
						# valid move
						outboard.cars[car.name].x -= 1
						outboard.update_current_state()
						return outboard

		# no valid moves
		return False
		

