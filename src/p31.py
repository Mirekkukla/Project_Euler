from datetime import datetime

def numWays(remains, theList):
    global tuples_seen
    if remains == 0:
        return 1
    else:
        total = 0
        for i in [200, 100, 50, 20, 10, 5, 2, 1]:
            if remains - i < 0:
                continue
            copyList = list(theList)
            copyList.append(i)
            copyList.sort()
            if not tuple(copyList) in tuples_seen:
                tuples_seen.add(tuple(copyList)) 
                total += numWays(remains - i, copyList)
        return total

startTime = datetime.now()
tuples_seen = set()
print(numWays(200, []))
print(datetime.now() - startTime)