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
        result = 0
        for i in range(0, math.floor(remains/highest) + 1):
            result += numWays(remains - i*highest, index - 1)
        return result

startTime = datetime.now()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(numWays(200, len(coins) - 1))
print(datetime.now() - startTime)