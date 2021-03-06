# this functions need to read a board file in a special format. 
# the functions returns a list with dict inside. 
# Rushhour


# creating a list to store the dictionary'

def main():
	path = "boards/01.txt"

	dim, lst = import_board(path)
	print(dim)
	print(lst)


def import_board(path):
	lst =  []

	# opening the board.txt file and reading it
	file = open(path, "r")
	if file == None:
		print("Opening dictionary file fialed")



	for line in file.readlines(): 
		if not line.startswith("#") or line.startswith(" ") or line.startswith("\n"):

			if line.startswith("dim:"):

				words = line.split()
				dim = words[1]

			else:
				words = line.split(',')

				# create dictionary 
				dic = {}

				# exstracting individuel words and putting them in a dict
				dic["name"] = words[0]
				dic["x"] = words[1]
				dic["y"] = words[2]
				dic["length"] = words[3]
				dic["orientation"] = words[4]

				lst.append(dic)

	file.close()

	return dim,lst

if __name__ == "__main__":
	main()



