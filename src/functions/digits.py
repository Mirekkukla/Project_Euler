from math import *

def getArrayFromNum(n):
    ret = []
    for i in range(0,numDigits(n)):
        digit = int(n/(pow(10,i))) % 10
        ret.append(digit)
    ret.reverse()
    return ret

def getNumFromArray(arr):
    copy_arr = list(arr)
    digits = len(copy_arr)
    result = 0
    copy_arr.reverse()
    for i in range(0,digits):
        result += copy_arr[i]*pow(10,i)
    return int(result)

def numDigits(n):
    return int(log10(n)) + 1

def getBinaryStrFromNum(n): 
    numBinDigits = (int(log(n,2)) + 1)
    ret = [0]*numBinDigits
    for i in range(numBinDigits):
        ret[i] = str(n % 2)
        n = n / 2
    ret.reverse()
    return ''.join(ret)
