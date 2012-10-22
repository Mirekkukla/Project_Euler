#Project Euler prob 20: p20.py
facNum = 100
import math

def cheating():
	result = reduce(lambda x,y: int(x)+int(y), str(math.factorial(facNum)));
	print(result)

def noCheating():
	numDigits = 0
	for i in range(1,facNum+1):
		numDigits += math.log(i,10)
	numDigits = int(numDigits)+1

	digits = [0]*numDigits #we'll write the number backwards in this array
	digits[0] = 1
	for i in range(1,facNum+1):
		digits = [i*n for n in digits]
		digits = carryOnes(digits)
	print(sum(digits))

def carryOnes(x):
	for i in range(len(x)):
		if x[i] > 9:
			x[i+1] += x[i]/10 #concats since their both ints
			x[i] = x[i]%10
	return x
