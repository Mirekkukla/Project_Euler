import math

def cycleLength(n):
    remainders = [1]
    exponent = 1
    r = 1
    while True:
        modresult = (r*(math.pow(10,exponent))) % n
        if modresult == 0: return -1 #not a repeating decimal
        if modresult == r*(10^exponent):
            exponent += 1
            remainders.append(modresult)
        else:
            already_seen = remainders.count(modresult)
            if already_seen != 0:
                remainder_location = remainders.index(modresult)
                return len(remainders) - remainder_location
            else:
                remainders.append(modresult)
                r = modresult
                exponent = 1
        
max_length = 0
max_d = 0
for i in range(2,1000):
    cur_length = cycleLength(i)
    if cur_length > max_length:
        max_length = cur_length
        max_d = i
print(max_d)