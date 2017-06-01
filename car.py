###############################################
# 
# Code written by: Julia Anten, Sander Swierts, Maxim Stomphorst
# 
# Defines Car class
#
###############################################


class Car(object):
	"""Defines Car class"""

	def __init__(self, name, x, y, length, orientation):
		"""Initializes the name, x and y coordinates, 
		length (either 2 or 3) and orientation.
		"""
		self.name = name
		self.x = x
		self.y = y
		self.length = length
		self.orientation = orientation

	def __repr__(self):
		"""Overrides standard repr method"""
		return "Car('" + self.name + "', " + str(self.x) + ", " + str(self.y)
		+ ", " + str(self.length) + ", '" + self.orientation + "')"
		
	def __hash__(self):
		"""Hashes a car by its name, x orientation, y orientation creating a long
		string that is converted to a integer because a hash has to retun a int.
		"""
		a_hash = []
		[a_hash.append(str(ord(character))) for character in self.name]
		a_hash.append(str(self.x))
		a_hash.append(str(self.y))
		return int("".join(a_hash))
	
	def __eq__(self, other):
		"""Overrides standard equals method"""
		return hash(self) == hash(other)
