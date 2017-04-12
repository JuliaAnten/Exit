class Car(object):
	"""Car gets a name, x and y coordinates, a length (either 2 or 3) 
	and an orientation. In orientation 1 represents horizontal and 0 
	represents vertical"""
	def __init__(self, name, x, y, length, orientation):
		self.name = name
		self.x = x
		self.y = y
		self.length = length
		self.orientation = orientation
		