import math

def isAbundant(n):
    total = 1
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if n/i != i: total += n/i
        if total > n: return True
    return False

setOfAbundant = set()
upperBound = 28123
for i in range(2,upperBound+1):
    if isAbundant(i): setOfAbundant.add(i)
    
mySet = set()
for i in setOfAbundant:
    for j in setOfAbundant:
        if i+j <= upperBound:
            mySet.add((i+j))

total = upperBound*(upperBound+1)/2
print(total-sum(mySet))