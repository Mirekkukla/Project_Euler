#Project Euler prob 6: p6.py
sumSquares = 0
squareSums = 0
for i in range(1, 101):
	sumSquares += i**2
	squareSums += i
squareSums = squareSums**2
print(squareSums - sumSquares)