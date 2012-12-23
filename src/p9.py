#Project Euler prob 9: p9.py

# Use a function so that we can break out of both loops
def findTriplet(p):
	for a in range(1,(p-2)+1):
		for b in range(a+1,(p-1)+1):
			c = p - (a + b)
			if a**2 + b**2 == c**2:
				return a*b*c
	return -1

print(findTriplet(1000))