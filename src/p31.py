from datetime import datetime
def numWays(remains, theList):
    global tuples_seen
    if remains == 0:
        return 1
    else:
        total = 0
        coins = [200, 100, 50, 20, 10, 5, 2, 1]
        for i in coins:
            if remains - i < 0: #not a viable combination
                continue
            copyList = list(theList)
            index = coins.index(i)
            copyList[index] += 1
            if not tuple(copyList) in tuples_seen:
                tuples_seen.add(tuple(copyList)) 
                total += numWays(remains - i, copyList)
        return total

startTime = datetime.now()
tuples_seen = set()
print(numWays(200, [0] * 8))
print(datetime.now() - startTime)