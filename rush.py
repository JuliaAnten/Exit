__eq_
!/usr/bin/env python3

# class Car:
# 	def __init__(self, id, size, orientation, location):
# 		self.id = id
# 		self.size = size
# 		self.orientation = orientation
# 		self.location = 

# 	# size
# 	# id
# 	# orientation
# 	# location
# 	# generate car

# Car car_arr[]

# size = 6

# def genBoard(size):
# 	board = [size][size]

# 	print

# x = (x**2 for x in range(20))
# print(x)

# x = list(x)
# print(x)

###################################

from board import Board

# height and width of the board
DIM = 6

# initialize empty board
board = [['-' for y in range(DIM)] for x in range(DIM)]

def main():

	# put red car on board
	board[2][3] = 'R'
	board[2][4] = 'R'

	# set orange 1
	board[4][0] = 'A'
	board[5][0] = 'A'

	# set orange 2
	board[3][4] = 'B'
	board[3][5] = 'B'

	# set orange 3
	board[3][3] = 'C'
	board[4][3] = 'C'
	board[5][3] = 'C'

	# set blue 1
	board[0][3] = 'D'
	board[0][4] = 'D'

	# set blue 2
	board[4][1] = 'E'
	board[4][2] = 'E'

	# set purple 1
	board[0][2] = 'F'
	board[1][2] = 'F'
	board[2][2] = 'F'

	# set yellow 1
	board[0][5] = 'G'
	board[1][5] = 'G'
	board[2][5] = 'G'

	# set green
	board[5][5] = 'H'
	board[5][4] = 'H'

	# draw current state of board
	draw_current()

	# ask for input
	print("Car to move")

		# ask for CarID and direction


# print board
def draw_current():
	for row in board:
		print(row)
	print("\n\n")

# make sure main is called
if __name__ == "__main__":
	main()