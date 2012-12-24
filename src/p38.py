#Loose upper limit for the multiplier number = 9876

#takes a string
def isPandigital(s):
    for i in range(1,9+1):
        if s.count(str(i)) == 1:
            continue
        else:
            return False
    return True
        
largest = 0
for i in range(1,9876 + 1):
    s = ''
    for p in range(1,9 + 1):
        s = s + str(i*p)
        if len(s) == 9:
            if isPandigital(s) and int(s) > largest:
                largest = int(s)
                print('found ' + s)
        if len(s) > 9:
            continue

print(largest)
                



