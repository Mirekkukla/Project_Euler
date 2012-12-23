# Project Euler prob 5: p5.py
from collections import Counter
from functions.primes import primeFactorization

req_primes = Counter()

for i in range(2, 20 + 1):
	i_primes = primeFactorization(i)
	for prime in i_primes:
		if req_primes[prime] < i_primes[prime]:
			req_primes[prime] = i_primes[prime]

result = 1
for prime in req_primes:
	result *= (prime**req_primes[prime])

print(result)