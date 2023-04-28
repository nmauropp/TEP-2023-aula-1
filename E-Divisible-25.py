# E - Make it Divisible by 25

# number of tests to be done
numberOfTests = int(input())

# description of the test cases
# for each test case
for i in range(numberOfTests):
	# define number of operations to be done
	operations = 0
	operationList = []
	# receive int input
	inputNumber = input()
	# see if it's visible by 25
	if(int(inputNumber)%25 == 0):
		print(operations)
		continue
	else:
		# check substrings
		for i in range(len(inputNumber)):
			# last numbers 25 or 75
			if(inputNumber[i]=='2' or inputNumber[i]=='7'):
				for j in range(i+1, len(inputNumber)):
					if(inputNumber[j]=='5'):

						# if number is 4259, we should remove the last number 9
						# operations = lenght - position of '5'
						# if number is 253, we should remove the last number 3
						# operations = lenght - position of '5'
						operations = len(inputNumber) - i
						operations = operations-2
						operationList.append(operations)
						

			if(inputNumber[i]=='5' or inputNumber[i]=='0'):
				for j in range(i+1, len(inputNumber)):
					if(inputNumber[j]=='0'):
						operations = len(inputNumber) - i
						operations = operations-2
						operationList.append(operations)
						
		if(operationList):
			operations = min(operationList)
			operationList.clear()
			print(operations)
			operations = 0
			continue;
		
