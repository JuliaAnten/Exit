#!/usr/bin/env python3

from car import Car
from board import Board

path = "boards/01.txt"


cars = [{"name": "red", "x": 0, "y": 2, "length": 2, "orientation": "h"},
		{"name": "a", "x": 3, "y": 2, "length": 2, "orientation": "v"},
		{"name": "b", "x": 4, "y": 4, "length": 2, "orientation": "h"}]

board = Board(6)

board.init_cars(cars)

for row in board.state:
	print(row)

board.init_cars(cars)

dim, cars = board.import_board(path)

print(dim)
print(cars)

print("+++++working???+++++")
board = Board(dim)

board.init_cars(cars)

for row in board.state:
	print(row)