# this functions need to read a board file in a special format. 
# the functions returns a list with dict inside. 
# Rushhour

lst =  []
dic = {}


file = open("boards/01.txt", "r")
if file == None:
	print("Opening dictionary file fialed")

for line in file.readlines(): 
	if not line.startswith("#") or line.startswith(" ") or line.startswith("\n"):

		if line.startswith("dim:"):
			words = line.split()
			dim = words[1]

		else:
			words = line.split(',')
			print(words)



