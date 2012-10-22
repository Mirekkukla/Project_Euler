#Project Euler prob 15: p15.py
n = 20 
iIter = range(n+1)
jIter = range(n+1)
iIter.reverse()
jIter.reverse()

d = {(n,n):1}
for i in iIter:
	for j in jIter:
		num = 0
		if i < n:
			num += d[(i+1,j)]
		if j < n:
			num += d[(i,j+1)]
		if (i,j) != (n,n):
			d.update({(i,j):num})
print(d[(0,0)])
