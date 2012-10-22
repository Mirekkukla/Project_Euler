#Project Euler prob 9: p9.py
import math
sum = 1000
maxNum = sum
breakAgain = False
for i in range(1,maxNum):
	for j in range(i+1,maxNum+1):
		if math.sqrt(i**2 + j**2) == sum - i - j:
			print(i*j*(sum-i-j))
			breakAgain = True
			break
	if breakAgain == True:
		break

