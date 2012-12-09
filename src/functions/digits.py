from math import *

def getDigits(n):
    ret = []
    for i in range(0,numDigits(n)):
        digit = int(n/(pow(10,i))) % 10
        ret.append(digit)
    ret.reverse()
    return ret

def numDigits(n):
    return int(log10(n)) + 1