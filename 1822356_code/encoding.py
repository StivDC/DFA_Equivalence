def encodingsDFA(file1):
	file1 = open(file1,"r+")
	newinp = file1.readlines()
	file1.close()
	for i in range(len(newinp)):
		newinp[i] = newinp[i].replace("\n","") # puts text file into list format for ease of access
	# print(newinp)
	numOfStates = int(newinp[0])
	dfa = {str(key): None for key in newinp[1].split(" ")} # makes eeach state a key in a dictionary for state

	sizeOfAlpha = int(newinp[2])
	alphabetK = [str(k) for k in newinp[3].split(" ")] # gets the alphabet as a list
	transFuncQ = []
	for i in range(1,numOfStates+1):
		transFuncQ.append([str(k) for k in newinp[i + 3].split(" ")]) # gets each transition function as a list
		if i == numOfStates:
			nline = i+4 # increments nline by 4 as there were 4 lines before the transition functions
	startS = str(newinp[nline])
	nOfendStates = int(newinp[nline+1])
	endStates = [str(k) for k in newinp[nline+2].split(" ")] # gets end states as list
	# print(statesN) debug lines
	# print(alphabetK)
	# print(transFuncQ)

	for i, key in enumerate(dfa): # go through states with index of each state
		dfa[key] = {K: Q for K, Q in zip(alphabetK, transFuncQ[i])} # creates a dictionary within the state dictionary
		# where each transition is stored with its corresponding value, e.g. {A: {'a': B, 'b': A}}

	return {'NumbOfStates': numOfStates, 'dfaSTF': dfa, 'sizeOfAlpha': sizeOfAlpha, 'AlphbetSpec': alphabetK,
	'startS': startS, 'nOfendStates': nOfendStates, 'endStates': endStates} # returns dictionary
