###############################################
# 
# Code written by: 
# - Julia Anten
# - Sander Swierts 
# - Maxim Stomphorst
# 
# This creates a Car Class where the information about the car's is stored.
#
###############################################

class Car(object):

	"""Car gets a name, x and y coordinates, a length (either 2 or 3) 
	and an orientation."""
	def __init__(self, name, x, y, length, orientation):
		self.name = name
		self.x = x
		self.y = y
		self.length = length
		self.orientation = orientation

	"""If print is called on car class is returns the following string,instead of the address
	instead of the address."""
	def __repr__(self):
		return "Car('" + self.name +"', " + str(self.x) + ", " + str(self.y) + ", " + str(self.length) + ", '" + self.orientation + "')"

		"""If hash is called on a car it hash a car by its name, x orientation, y orientatino
		creating a long string that is converted to a interger because a hash has to retun a int."""
	def __hash__(self):
		a_hash = []
		[a_hash.append(str(ord(character))) for character in self.name]
		a_hash.append(str(self.x))
		a_hash.append(str(self.y))
		return int("".join(a_hash))

	"""If a equality test is called on the class 
	this determines how it is handelt."""
	def __eq__(self, other):
		return hash(self) == hash(other)