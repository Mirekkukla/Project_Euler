#project Euler prob 7: p7/py
from functions.primes import isPrime

i = 1
count = 0
while True:
	if isPrime(i):
		count += 1
	if count == 10001:
		break
	i += 1
print(i)