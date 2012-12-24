from functions.digits import *
from functions.primes import *

prime_set = set()
limit = 1000000

for i in range(2,limit + 1):
    len = numDigits(i)
    cand = i
    isCircular = True
    for p in range(1,len + 1):
        if not isPrime(cand):
            isCircular = False
            break
        cand = int(s(cand)[-1] + s(cand)[0:-1])
        if cand < i:
            isCircular = False
            break;
    if isCircular:
        cand = i
        prime_set.add(cand)
        for p in range(1,len + 1):
            cand = int(s(cand)[-1] + s(cand)[0:-1])
            prime_set.add(cand)
print(prime_set.__len__())
    
        
    