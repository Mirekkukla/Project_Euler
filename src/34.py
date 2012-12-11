from math import *
from functions.digits import numDigits

#VERY loose lower bound on number we have to check:
#don't need to check a number higher than 10^k, #where 1*10^k >= (9!)*(k-1)
#(if we add any higher digits, the number will always be larger than the
#factorial digit total)

fact_list = []
sum_matrix = []
max_pows_of_ten = 0

#find bound on number of digts we have to check
k = 2
while True:
    if pow(10,k) >= factorial(9)*(k-1):
        max_pows_of_ten = k
        break
    k += 1
print("total digit limit is " + str(max_pows_of_ten))

#cache numbers we'll use in our recursion
def setupArrays():
    global fact_list
    global sum_matrix
    global max_pows_of_ten
    for i in range(0,10):
        fact_list.append(factorial(i))
    
    for i in range(0,10):
        row = []
        for j in range (0,max_pows_of_ten):
            row.append(int(i*pow(10,j)))
        sum_matrix.append(row)

#naive way is fast enough
#try powers of ten in highest to lowes order (ex if total_pows_of_ten = 3, try X__, then XY_, then XYZ)
def recurseDigits(fact_total, sum_total, last_filled_pow_of_ten, total_pows_of_ten):
    global fact_list
    global sum_matrix
    if last_filled_pow_of_ten == 0:
        if fact_total == sum_total and numDigits(sum_total) == total_pows_of_ten: # cant haveleading zeros
            print("found " + str(fact_total) + " with " + str(total_pows_of_ten) + " digit limit")
            return fact_total
        else:
            return 0
    else:
        total = 0
        for i in range(0,10):
            total += recurseDigits(fact_total + fact_list[i], sum_total + sum_matrix[i][last_filled_pow_of_ten - 1],
                                   last_filled_pow_of_ten - 1, total_pows_of_ten)
        return total

setupArrays()
total = 0
for i in range(2, max_pows_of_ten + 1):
    total += recurseDigits(0,0,i, i)
print("total of all is special numbers is " + str(total))
