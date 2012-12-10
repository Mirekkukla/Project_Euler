from math import *

def getArrayFromNum(n):
    ret = []
    for i in range(0,numDigits(n)):
        digit = int(n/(pow(10,i))) % 10
        ret.append(digit)
    ret.reverse()
    return ret

def getNumFromArray(arr):
    digits = len(arr)
    result = 0
    arr.reverse()
    for i in range(0,digits):
        result += arr[i]*pow(10,i)
    return int(result)

def numDigits(n):
    return int(log10(n)) + 1