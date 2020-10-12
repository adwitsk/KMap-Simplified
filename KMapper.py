from copy import deepcopy

def remDuplicate(x):
	""" Removes duplicate items from a list. """
  # TODO

def countOnes(num):
	""" Counts the number of '1's in the binary representation of an integer. """
  # TODO

def compareBin(matrix, var):
	""" Used to create a matrix of binary numbers which differ by only one digit by replacing that digit with a '-'. """

	newmatrix = []
	for i in range(var):
		newmatrix.append([])

	n=0																	# Finding the position of binary sublist in the matrix
	for x in matrix:
		for y in x:
			for z in y:
				if type(z)==list:
					n=y.index(z)

	temp = 0
	for i in range(len(matrix)-1):										# Checks for each group of '1's
		e = 0
		for f in range(len(matrix[i])):
			for g in range(len(matrix[i+1])):
				count = 0
				for l in range(var):
					if matrix[i][f][n][l]!=matrix[i+1][g][n][l]: 		# Comparing digits of binary numbers of adjacent groups of '1's
						count+=1
						if count==1:
							temp=l
				if count==1:											# If only one digit differs in the binary numbers

					matrix[i][f][-1] = True								# Flag changed to true
					matrix[i+1][g][-1] = True
					newmatrix[i].append([])
					newmatrix[i][e].extend(matrix[i][f][:n])			# Combining the minterms
					newmatrix[i][e].extend(matrix[i+1][g][:n])
					a = deepcopy(matrix[i][f][n])
					a[temp] = '-'										# Replacing the different bit with a '-'
					newmatrix[i][e].append(a)
					newmatrix[i][e].append(False)
					newmatrix[i][e][:2*n] = sorted(newmatrix[i][e][:2*n])
					e += 1
		matrix[i] = remDuplicate(matrix[i])								# Removing duplicate items
					
	return newmatrix
	

def convertIntoVar(matrix):
	""" Converts binary numbers to variable representation. """

	ans = ""
	for i in matrix:
		for j in range(len(i[-2])):										# Checks all numbers before the binary representation list
			if j == 0:													# Eg: [[0, 1, 2, 3, ['0', '-', '-'], False]
				if i[-2][j] == '0':
					ans += "w'"
				if i[-2][j] == '1':
					ans += "w"
			if j == 1:
				if i[-2][j] == '0':
					ans += "x'"
				if i[-2][j] == '1':
					ans += "x"
			if j == 2:
				if i[-2][j] == '0':
					ans += "y'"
				if i[-2][j] == '1':
					ans += "y"
			if j == 3:
				if i[-2][j] == '0':
					ans += "z'"
				if i[-2][j] == '1':
					ans += "z"
		ans += "+"
	ans = ans[:-1]
	if ans == "":
		return "1"
	return ans




def minFunc(numVar, stringIn):
	"""
        This python function takes function of maximum of 4 variables
        as input and gives the corresponding minimized function(s)
        as the output (minimized using the K-Map methodology),
        considering the case of Don’t Care conditions.

	Input is a string of the format (a0,a1,a2, ...,an) d(d0,d1, ...,dm)
	Output is a string representing the simplified Boolean Expression in
	SOP form.

	"""
	
	index = stringIn.find('d')
	minterms = list(map(int, stringIn[1:index-2].split(',')))					# Creating a list of minterms
	if stringIn[index+1] == '-':
		dont_cares = []
	else:
		dont_cares = list(map(int, stringIn[index+2:-1].split(',')))			# Creating a list of don't-cares

	MATRIX1 = []
	for i in range(numVar+1):
		MATRIX1.append([])
		
	s = "{" + ":0%db"%numVar + "}"												# For binary representation according to the number of variables used

	for i in minterms+dont_cares:
		MATRIX1[countOnes(i)].append([i])
		MATRIX1[countOnes(i)][MATRIX1[countOnes(i)].index([i])].append(list(s.format(i)))

	for i in range(numVar+1):													# Adding the flags
		for j in MATRIX1[i]:
			j.append(False)

	MATRIX2 = compareBin(MATRIX1, numVar)										# One possible bit removed
	MATRIX3 = compareBin(MATRIX2, numVar)										# Two possible bits removed
	MATRIX4 = compareBin(MATRIX3, numVar)										# Three possible bits removed
	MATRIX5 = compareBin(MATRIX4, numVar)										# Four possible bits removed

	PI = []																		# List of Prime Implicants (whose flag is False)
	for i in MATRIX1 + MATRIX2 + MATRIX3 + MATRIX4 + MATRIX5:
		for j in i:
			if j[-1]==False:
				PI.append(j)
	
	EPI = []																	# List of Essential Prime Implicants																
	for i in minterms:
		count = 0
		temp = 0
		for j in PI:															# Checks each minterm in the list of PI
			for k in range(len(j)):	
				if i==j[k] and type(j[k])!=bool:
					count+=1
					if count==1:
						temp=PI.index(j)				
		if count==1:															# If any minterm is only covered by one PI,
			EPI.append(PI[temp])												# that PI is an EPI
	EPI = remDuplicate(EPI)
	
	NonEPI = [x for x in PI if x not in EPI]									# All PI not EPI are NonEPI
	NonEPI = remDuplicate(NonEPI)

	LeftOut = []																# Minterms which are not covered by the EPI
	for x in minterms:															# For them, extra NonEPI will be used along with the EPI
		flag = 1
		for y in EPI:
			if x in y:
				flag = 0
		if flag:
			LeftOut.append(x)
	
	if len(LeftOut)!=0:															# If any terms are leftout, there could be multiple answers
		s = ""
		while len(NonEPI)!=0:
			Ans = deepcopy(EPI)
			for x in LeftOut:													# Checking which NonEPI to use for the left out minterm
				for y in range(len(NonEPI)):
					if x in NonEPI[y]:
						NonEPI[y][-1]=True
						break
			for x in NonEPI:
				if x[-1]:
					Ans.append(x)
			for i in NonEPI:
				if i[-1]:
					NonEPI.remove(i)											# Removing the NonEPI so that it is not reused
			s+=(convertIntoVar(Ans)) + " OR "
		s = s[:-4]
		return s
	else:
		return(convertIntoVar(EPI))

if __name__ == "__main__":
	var = int(input("Enter number of variabes: "))
	a = input("Enter Minterms and Don’t Cares: ")
	print("SIMPLIFIED EXPRESSIONS: ", end="")
	print(minFunc(var,a))
