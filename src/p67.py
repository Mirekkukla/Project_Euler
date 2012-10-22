#Project Euler prob 67: p67.py
#copied the code for p18

#import data
filename = 'p67data'
f = open(filename, 'r')
ystrings = []
for line in f:
	ystrings.append(line[0:len(line) - 1])
hight = len(ystrings)

#convert chars to ints
for i in range(hight):
	ystrings[i] = ystrings[i].split(' ')
yrows = [[int(digit) for digit in row] for row in ystrings] 

#make entries accessible in cartesian coordinates, bottom left is 0,0
def P(x,y):
	return yrows[hight - y - 1][x]

#store the running sums
d = {(0,hight-1):P(0,hight-1)}
yitover = range(hight)
yitover.reverse()
for y in yitover:
	for x in range(hight):
		if x + y <= hight - 1:
			ul = 0; u = 0; ur = 0
			if x > 0:
				#legal to go up left
				ul = d[(x-1, y+1)]
			if x + y <= hight - 2:
				#legal to go up
				u = d[(x,y+1)]
			d.update({(x,y):P(x,y)+max(ul,u,ur)})

#print the largest running sum from bottom row
largest = 0
for i in range(hight):
	if d[(i,0)] > largest:
		largest = d[(i,0)]
print(largest)
