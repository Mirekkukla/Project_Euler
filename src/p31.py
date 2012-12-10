from datetime import datetime
import math

# in each recursive call, only use coins smaller than the ones just tried
def numWays(remains, index):
    global coins
    if remains < 0 or (index == -1 and remains > 0):
        return 0
    elif remains == 0:
        return 1
    else:
        highest = coins[index]
        total = 0
        for i in range(0, math.floor(remains/highest) + 1):
            total += numWays(remains - i*highest, index - 1)
        return total

startTime = datetime.now()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(numWays(200, len(coins) - 1))
print(datetime.now() - startTime)