from datetime import datetime
import math

# in each recursive call, only use coins smaller than the ones just tried
def numWays(remains, coins):
    if remains < 0 or (len(coins) == 0 and remains > 0):
        return 0
    elif remains == 0:
        return 1
    else:
        highest = coins.pop()
        total = 0
        for i in range(0, math.floor(remains/highest) + 1):
            coins_copy = list(coins)
            total += numWays(remains - i*highest, coins_copy)
        return total

startTime = datetime.now()
coins = [1, 2, 5, 10, 20, 50, 100, 200]
print(numWays(200, coins))
print(datetime.now() - startTime)