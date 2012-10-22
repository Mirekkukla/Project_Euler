#Project Euler prob 10: p10.py
import math
primes = []
last = 2000000
result = 0
for i in range(2, last+1):
	itsPrime = True
	for j in primes:
		if (i%j == 0): 
			itsPrime = False
			break
		if j > int(math.sqrt(i)):
			break
	if itsPrime:
		primes.append(i)
		result = result + i
print(result)
			
				
