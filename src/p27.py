#project Euler prob 27
#just brute force it, but cache prime results
from functions.primes import *

bestPair = (0,0)
bestStreak = 0
d = {} #says whether a number is prime or not
upperLimit = 79

for a in range(-1000,1000):
    for b in range(-1000,1000):
        n = 0
        for n in range(0,upperLimit + 1):
            candidate = n*n + a*n + b
            if candidate < 2:
                break
            if not candidate in d:
                d[candidate] = isPrime(n*n + a*n + b)
            if d[candidate] == False:
                break
        if n - 1 > bestStreak:
            bestStreak = n - 1
            bestPair = (a,b)
print(bestPair)
print(bestPair[0]*bestPair[1])