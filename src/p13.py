#Project Euler prob 13: p13.py
def cheating():
	filename = "p13data"
	f = open(filename, 'r')
	sum = 0
	for line in f:
		sum += int(line)
	print(str(sum)[0:10])

def noCheating():
	#import data
	filename = "p13data"
	f = open(filename, 'r')
	nums = []
	for line in f:
		nums.append(line) #imports them as strings
	first10 = []
	sumofd = [0]*50
	carry = 0
	for i in range(50):
		for curline in nums:
			sumofd[i] += int(curline[49-i])
		sumofd[i] = sumofd[i] + carry
		carry = sumofd[i]/10 #we have 2 ints, automatically concats
	numdigs =  len(str(sumofd[49]))
	for i in range(numdigs):
		first10.append(int(str(sumofd[49])[i]))
	i = 0
	while len(first10) < 10:
		first10.append(sumofd[48-i]%10)
		i += 1
	print(first10)
