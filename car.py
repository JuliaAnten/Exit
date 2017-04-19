class Car(object):
	"""Car gets a name, x and y coordinates, a length (either 2 or 3) 
	and an orientation."""
	def __init__(self, name, x, y, length, orientation):
		self.name = name
		self.x = x
		self.y = y
		self.length = length
		self.orientation = orientation

	# a car object is printed like this and not with the adress
	def __repr__(self):
		return "Car('" + self.name +"', " + str(self.x) + ", " + str(self.y) + ", " + str(self.length) + ", '" + self.orientation + "')"