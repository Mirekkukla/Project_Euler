from functions.primes import *
from functions.digits import *

#pass dir = 'R' or 'L'
def isSpecial(n, dir):
    nStr = s(n)
    while True:
        if nStr == '':
            return True
        if not isPrime(int(nStr)):
            return False
        else:
            if dir == 'R':
                nStr = nStr[0:-1]
            else:
                nStr = nStr[1:]
numFound = 0
score = 0
i = 8
while True:
    if numFound >= 11:
        break
    if(isSpecial(i, 'L') and isSpecial(i, 'R')):
        print(i)
        score += i
        numFound += 1
    i += 1

print('sum is ' + s(score))
        


        