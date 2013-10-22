#Project Euler Prob 12: p12.py
from math import sqrt, floor
from datetime import datetime

def nthTriag(n):
	return int(n*(n+1)/2)

def numFacs(n):
	num = 0
	for i in range(1, floor(sqrt(n)) + 1):
		if n % i == 0:
			num += 1
	num *= 2
	if int(sqrt(n))**2 == n: #its root is a factor
		num -= 1 
	return num

startTime = datetime.now()
factors_wanted = 500
i = 1
while True:
	triag_num = nthTriag(i)
	factors = numFacs(triag_num)
	if factors > factors_wanted:
		break
	i += 1
print(nthTriag(i))
print(datetime.now() - startTime)