# input n value
numberOfTests = int(input())

for i in range (numberOfTests):
	# variable to determinate if there is a triple draw between all candidates
	tripleDraw = 0
	# votes to win
	votesLeftToWin = []
	votesList = input()
	votes = votesList.split(" ")
	# string to int
	votesInt = []
	for j in range(len(votes)):
		votesInt.append(int(votes[j]))
	# winner votes
	winner = max(votesInt)
	# candidate A
	if votesInt[0] == winner:
		candidateA = 0
	else:
		candidateA = winner - votesInt[0] 
		candidateA += 1

	# candidate B
	if votesInt[1] == winner:
		candidateB = 0
	else:
		candidateB = winner - votesInt[1]
		candidateB += 1

	# candidate C
	if votesInt[2] == winner:
		candidateC = 0
	else:
		candidateC = winner - votesInt[2]
		candidateC += 1

	# draw between all candidates
	if votesInt[0] == votesInt[1]== votesInt[2]:
		candidateA += 1
		candidateB += 1
		candidateC += 1
		# there is a draw between all candidates
		tripleDraw = 1

	# draw between two if the third one already lost the election
	if(not tripleDraw):
		# draw between two candidates (A and B)
		if votesInt[0] == votesInt[1] and votesInt[0] == winner:
			candidateA += 1
			candidateB += 1

		# draw between two candidates (B and C)
		if votesInt[1] == votesInt[2] and votesInt[1] == winner:
			candidateB += 1
			candidateC += 1

		# draw between two candidates (A and C)
		if votesInt[0] == votesInt[2] and votesInt[2] == winner:
			candidateA += 1
			candidateC += 1

	print(str(candidateA) + " " + str(candidateB) + " " + str(candidateC))