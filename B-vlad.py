# B - VLAD AND CANDIES 
#input n value
numberOfTests = int(input())

# description of the test cases
for i in range(numberOfTests):

	# number of types 
	numberOfTypes = int(input())

	# number of candies of each type
	numberOfCandies = input()

	# in case we only have 1 type
	if(numberOfTypes == 1):
		numberOfCandies = int(numberOfCandies)
		if(numberOfCandies > 1):
			print("NO")
		else: print("YES")
	else:
		numberOfCandies = list(map(int,numberOfCandies.split()))
		frequent1 = max(numberOfCandies)
		numberOfCandies.remove(frequent1)
		frequent2 = max(numberOfCandies)
		if(frequent1 - frequent2 <= 1):
			print("YES")
		else:
			print("NO") 