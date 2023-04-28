# input n value
numberOfTests = int(input())

# description of the test cases
for i in range(numberOfTests):
	sequence = input()
	numberOfZeros = sequence.count('0')
	numberOfOnes = sequence.count('1')

	if numberOfOnes > numberOfZeros:
		print(numberOfZeros)

	if numberOfZeros > numberOfOnes:
		print(numberOfOnes)

	if (numberOfOnes == numberOfZeros):
		print(numberOfOnes-1)