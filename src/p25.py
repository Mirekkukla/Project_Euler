import math
nm2 = 1
nm1 = 1
term = 2

while True:
    temp = nm1 + nm2
    nm1 = nm2
    nm2 = temp
    term = term + 1
    if math.ceil(math.log(temp,10)) == 1000:
        print(term)
        break
