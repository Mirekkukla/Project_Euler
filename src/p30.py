from math import *
from functions.digits import *
import functools

exponent = 5
highest_pos = -1

# once k*(9^exponent) has > k digits, we have an upper limit
k = 1
num_digits = 1
while k <= num_digits:
    k += 1
    num_digits = numDigits(k*pow(9,exponent))
    highest_pos = pow(9,exponent)*num_digits

total_sum = 0
for i in range(2,int(highest_pos) + 1):
    digits = getArrayFromNum(i)
    i_sum = 0
    for d in digits:
        i_sum += pow(d,exponent)
    if i_sum == i:
        total_sum += i
print(total_sum)
    