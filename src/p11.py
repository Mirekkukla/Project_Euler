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
	for p in range(numCols):	
		rows[i][p] = int(rows[i][p])

maxProd = 0
for i in range(numRows):
	for p in range(numCols):
		tempL = 1
		tempLD = 1
		tempD = 1
		tempRD = 1
		for k in range(4):
			if ((p-3+k) >= 0) and ((p-3+k) <= (numCols - 1)):
				tempL *= rows[i][p-3+k]
				if ((i+3-k) >= 0) and ((i+3-k) <= (numRows - 1)):
					tempLD *= rows[i+3-k][p-3+k]

			if ((i+k) >=0) and ((i+k) <= (numRows - 1)):
				tempD *= rows[i+k][p]
				if ((p+k) >= 0) and ((p+k) <= (numCols - 1)):
					tempRD *= rows[i+k][p+k]

		biggestHere = max_prod([tempL, tempLD, tempD, tempRD]) 
		if biggestHere > maxProd:
			maxProd = biggestHere
print(maxProd)
