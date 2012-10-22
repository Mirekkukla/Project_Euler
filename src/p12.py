#Project Euler Prob 12: p12.py
def nthTriag(n):
	return n*(n+1)/2

import math
def numFacsFast(n):
	root = math.sqrt(n)
	upperRange = (int)(math.floor(root)+1)
	num = 0
	for i in range(1, upperRange):
		if n % i == 0:
			num += 1
	if root % 1 == 0: #its root is a factor
		num = (num - 1)*2
		num += 1
	else:
		num *= 2
	return num

def doit(rangeStart,rangeEnd,facsWanted):
	maxTriagIndex = 1
	maxTriag = 1
	maxFacs = 1
	for i in range(rangeStart, rangeEnd + 1):
		tempTriag = nthTriag(i)
		tempFacs = numFacsFast(tempTriag)
		if tempFacs > maxFacs:
			maxTriag = tempTriag #the ith tiang num had the most
			maxTriagIndex = i
			maxFacs = tempFacs
			if maxFacs > facsWanted:
				break
	print("it was the ", maxTriagIndex, "th triangle number, ie ", maxTriag, " and it had ", maxFacs, " factors")
