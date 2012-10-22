#Project Euler prob 11: p11.py
rows = []
f = open("p11data", 'r')
for line in f:
	rows.append(str(line))
for i in range(len(rows)):
	rows[i] = rows[i][0:len(rows[i])-1]#take off the endline chars
numRows = len(rows)
numCols = numRows #assuming we have an nxn array

#make the input be ints instead of strings
for i in range(numRows):
	rows[i] = rows[i].split(' ')
	for j in range(numCols):	
		rows[i][j] = int(rows[i][j])

maxProd = 0
for i in range(numRows):
	for j in range(numCols):
		tempL = 1
		tempLD = 1
		tempD = 1
		tempRD = 1
		for k in range(4):
			if ((j-3+k) >= 0) and ((j-3+k) <= (numCols - 1)):
				tempL *= rows[i][j-3+k]
				if ((i+3-k) >= 0) and ((i+3-k) <= (numRows - 1)):
					tempLD *= rows[i+3-k][j-3+k]

			if ((i+k) >=0) and ((i+k) <= (numRows - 1)):
				tempD *= rows[i+k][j]
				if ((j+k) >= 0) and ((j+k) <= (numCols - 1)):
					tempRD *= rows[i+k][j+k]

		biggestHere = max([tempL, tempLD, tempD, tempRD]) 
		if biggestHere > maxProd:
			maxProd = biggestHere
print(maxProd)
