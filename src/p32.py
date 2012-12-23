from datetime import datetime
from functions.digits import getNumFromArray

def allPand(arr):
    global products
    if len(arr) == 9:
        addIfPand(arr)
    else:
        remainders = list(range(1,10))
        for i in arr:
            remainders.remove(i)
        for p in remainders:
            arr_copy = list(arr)
            arr_copy.append(p)
            allPand(arr_copy)

def addIfPand(arr):
    for i in range(1,5): #mult sign is right before this
        a = getNumFromArray(arr[0:i])
        b = getNumFromArray(arr[i:5])
        c = getNumFromArray(arr[5:9]) #product must be last 4 digits
        if a * b == c:
            products.add(c)

startTime = datetime.now()
products = set()
allPand([]) #recursively find every permutation, check each
print(sum(products))
print(datetime.now() - startTime)