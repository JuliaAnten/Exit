#!/usr/bin/env python3

# dimension of the board (so that the car can get out of the area)
dimensions = 6

class Car():    
    def __init__(self): #(,x,y)
        # Each Car has an (x,y) position.
        self.x = 0
        self.y = 0
        
    def move_verical(self):
        # Increment the y-position of the rocket.
        if self.y == dimensions:
        	return print("max y dimensions")
        self.y += 1

    def move_horizontal(self):
        # Increment the x-position of the rocket.
        if self.x == dimensions:
        	return print("max x demensions")
        self.x += 1

my_car = Car()
for i in range(7):
	my_car.move_verical()
	my_car.move_horizontal()

print(my_car.y)


print(my_car.x)

