import math
import collections

def isPrime(n):
    for i in range(2,math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primeFactorization(n):
    cnt = collections.Counter()
    for i in range(2,math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            cnt[i] += 1
            return cnt + primeFactorization(int(n / i))
    return collections.Counter([n])