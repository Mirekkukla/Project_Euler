#Project Euler prob 11: p11.py

#takes 4x4 array of nums, returns the max
#same-direction-product
def getBoxMax(A):
	box_max = 0
	down_diag = up_diag = 1
	for i in range(4):
		down_diag *= A[i][i]
		up_diag *= A[i][3-i]
		row_i = col_i = 1
		for j in range(4):
			row_i *= A[i][j]
			col_i *= A[j][i]
		box_max = max(box_max, row_i, col_i)
	box_max = max(box_max, up_diag, down_diag)
	return box_max

def importData():
	rows = []
	f = open("files/p11data", 'r')
	for line in f:
		row = line.strip().split(' ')
		for i in range(len(row)):
			row[i] = int(row[i])
		rows.append(row)
	return rows

rows = importData()
numRows = len(rows)
global_max = 0
for i in range(numRows - 3):
	for j in range(numRows - 3):
		A = rows[i:i+4]
		for k in range(4):
			A[k] = A[k][j:j+4]
		box_max = getBoxMax(A)
		if box_max > global_max:
			global_max = box_max
print(global_max)