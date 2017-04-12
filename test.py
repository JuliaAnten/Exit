from car import Car
from board import Board

# cars = []

# cars[0] = Car("red", 0, 0, 2, "v")

# print(red.x)

board = Board(6)

board.make()

for row in board.state:
	print(row)