from functions.digits import *

prod = 1
wanted_digit_list = [1000000,100000,10000,1000,100,10,1]
digit_count = 0
i = 0

while True:
    i += 1
    if not wanted_digit_list:
        break
    next_wanted_digit = wanted_digit_list[-1]
    
    if digit_count <= next_wanted_digit:
        if digit_count + numDigits(i) >= next_wanted_digit:
            prod *= int(str(i)[next_wanted_digit - digit_count - 1])
            wanted_digit_list.pop()
        digit_count += numDigits(i)
print(prod)