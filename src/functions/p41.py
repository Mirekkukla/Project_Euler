from functions.primes import *

def permutation(so_far_str, rest_arr, n):
    if len(so_far_str) == n:
        if isPrime(int(so_far_str)):
            print(so_far_str + ' is prime')
    for digit in rest_arr:
        copy_arr = list(rest_arr)
        copy_arr.remove(digit)
        permutation(so_far_str + str(digit), copy_arr, n)

for i in reversed(range(1,9 + 1)):
    arr = list(range(1,i+1))
    arr.reverse()
    print('now doing ',arr, i)
    permutation('', arr, i)