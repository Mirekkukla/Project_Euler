from functions.digits import *
import math

# assumes a/b < 1
def lowestTerms(arr):
    a = arr[0]
    b = arr[1]
    for i in reversed(range(2, a + 1)):
        if a % i == 0 and b % i == 0:
            return [int(a / i), int(b / i)]
    return [a, b]

#first elem in array is fraction is the one that gets 'canceled'
#arr is [[a,b], [c,d]]. Assume [a,b] is in form xx/xx, [c,d] in form x/x
def isCurious(arr):
    [a,b] = arr[0]
    [c,d] = arr[1]
    top = getArrayFromNum(a)
    bot = getArrayFromNum(b)
    if a % 10 == 0: # trivial example (zeros cancel)
        return False
    for i in range(0,2):
        for p in range(0,2):
            if top[i] == bot[p] and top[int(math.fabs(i - 1))] == c and bot[int(math.fabs(p - 1))] == d:
                return True
    return False

def hasCuriousPartner(arr):
    a = arr[0]
    b = arr[1]
    [a_low, b_low] = lowestTerms(arr)
    for i in range(1,10):
        # curious partner has to be in form x/x
        if i * b_low >= 10 or i * b_low >= b :
            break
        if isCurious([[a,b], [a_low * i, b_low * i]]):
            return True
    return False
    
def setOfCurious():
    candidates = set()
    for i in range(10, 99): #numerator
        for p in range(i + 1, 100): #denominator
            if hasCuriousPartner([i,p]):
                candidates.add(tuple([i,p]))
    return candidates

candidates = setOfCurious()
print(candidates)
product = [1, 1]

for item in candidates:
    product[0] *= item[0]
    product[1] *= item[1]
print(product, lowestTerms(product))
