from functions.digits import *
import math

def isPalindrome(n):
    s = s(n)
    for i in range(0, int(len(s) / 2)):
        if not s[i] == s[-(i+1)]:
            return False
    return True

def inBinary(n):
    remain = n
    ret = 0
    while remain > 0:
        k = int(math.floor(math.log(remain,2)))
        remain = remain - int(pow(2,k))
        ret += int(math.pow(10,k))
    return int(ret)

highest = int(pow(10,6))
result = 0
for i in range(1, highest + 1):
    if isPalindrome(i):
        base2 = inBinary(i)
        if isPalindrome(base2):
            result += i

print(result)
            