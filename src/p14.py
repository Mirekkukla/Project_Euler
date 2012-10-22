#Project Euler prob 14: p14.py
def f(n):
	if n%2 == 0:
		return n/2
	else:
		return 3*n+1

def doit():
	maxlen = 0
	best = 0
	d = {2:1}
	for i in range(3,1000000):
		curlen = 1 
		curnum = i
		while curnum != 1:
			curnum = f(curnum)
			curlen += 1
			if curnum < i:
				curlen += d[curnum]#diclookup len for startum
				d.update({i:curlen})
				curnum = 1 
		if curlen > maxlen:
			maxlen = curlen
			best = i
	print('best is: %d and len is: %d ' % (best, maxlen))
