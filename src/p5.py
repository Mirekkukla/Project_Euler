# Project Euler prob 5: p5.py

def getFacs(n):
	facs = []
	rest = n
	for i in range(2, n+1):
 		while True:
			if rest%i == 0:
				facs.append(i)
				rest = rest/i
			else:
				break
		if rest == 1:
			break
	return facs

def doit():
	primes = [2,3,5,7,11,13,17,19]
	maxOccur = [0,0,0,0,0,0,0,0]
	tempFacs = []
	for i in range(2,21):
		tempFacs = getFacs(i)
		occurences = 0
		for j in range(len(primes)):
			occurences = tempFacs.count(primes[j])
			if occurences > maxOccur[j]:
				maxOccur[j] = occurences
	output = 1
	for i in range(len(primes)):
		output *= (primes[i]**maxOccur[i])
	print(maxOccur)
	print(output)
	print(maxOccur)
	print(primes)
