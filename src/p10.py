#Project Euler prob 10: p10.py
import math
from datetime import datetime
from functions.primes import *
last = 2000000

# Sieve method
def memoryHog():
	s = ['0']*(last + 1) #index i represent number i
	for i in range(2,last+1):
		if s[i] == '0':
			for j in range(2, math.ceil(last / i)):
				s[i*j] = '1'
	s[0] = s[1] = s[last - 1] = '1'
	
	result = 0
	for i in range(last):
		if s[i] == '0':
			result += i
	print(result)

# Primality testing
def timeHog():
	result = 2
	primes = [2]
	for i in range(3, last+1, 2): #only check odds
		isPrime = True
		for p in primes:
			if p > math.floor(math.sqrt(i)):
				break
			if (i % p == 0):
				isPrime = False
				break
		if isPrime:
			primes.append(i)
			result = result + i
	print(result)


startTime = datetime.now()
timeHog()
print(datetime.now() - startTime)

