from math import sqrt, floor
import collections

def isPrime(n):
    if n == 1:
        return False
    for i in range(2,floor(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Returns a counter of prime factors - ie, a dictionary
# that maps each prime factors to it number of occurences
def primeFactorization(n):
    return __smartPrimeFactorization(n,2)

# Don't re-check small number we know are divisors
def __smartPrimeFactorization(n, smallest_cand):
    req_primes = collections.Counter()
    for i in range(smallest_cand,floor(sqrt(n)) + 1):
        if n % i == 0:
            req_primes[i] += 1
            return req_primes + __smartPrimeFactorization(int(n / i), i)
    return collections.Counter([n]) #n is a prime