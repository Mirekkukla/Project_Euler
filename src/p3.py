#Project Euler Problem 3: p3.py
from functions.primes import primeFactorization
prods = []
num =  600851475143

max_factor = 0
req_primes = primeFactorization(num)
for factor in req_primes:
	if factor > max_factor:
		max_factor = factor
print(max_factor)