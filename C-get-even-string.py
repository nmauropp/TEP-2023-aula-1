# input n value
numberOfTests = int(input())

# the input string to be read
def removeEven(string):
	evenNumbersToRemove = 0
	removeList = ""
	size = len(string)

	for j in string:
		if j in removeList:
			size -= 2
			removeList = ""
		else:
			removeList = removeList + j
	return size

# description of the test cases
for i in range(numberOfTests):

	# function to calculate how many characters should be removed
	print(removeEven(input()))
	


	