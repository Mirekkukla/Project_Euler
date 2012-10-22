#Project Euler Problem 3: p3.py
import math
prods = []
num =  600851475143
rest = num
temp = 1
last = int(math.floor(math.sqrt(num)))
for i in range(2,last+1):
	temp = 1
	for j in prods:
		temp = temp*j
	if temp == num:
		break
	same = 0
	while same == 0:
		if rest % i == 0:
			rest = rest/i
			prods.append(i)
		else:
			same = 1
print(prods)
if temp == num:
	print('its the max of the above')
else:
	print('use the above to find the max')
