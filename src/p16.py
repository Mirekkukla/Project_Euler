#Project Euler prob 16: p16.py
base = 2
power = 1000
import math

def cheating():
	result = reduce(lambda x,y: int(x)+int(y), str(base**power));
	print(result)

def noCheating():
	numDigits = int(power*math.log(base,10))+1
	digits = [0]*numDigits #we'll write the number backwards in this array
	digits[0] = 2
	for i in range(1,power):
		digits = [2*n for n in digits]
		digits = carryOnes(digits)
	print(sum(digits))

def carryOnes(x):
	for i in range(len(x)):
		if x[i] > 9:
			x[i+1] += x[i]/10 #concats since their both ints
			x[i] = x[i]%10
	return x
