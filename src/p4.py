#Project Euler prob 4: p4.py
from functions.words import isPalindrome

largest_pal = 0
for i in range(100, 999 + 1):
	for p in range(i, 999 + 1):
		prod = i*p
		if prod > largest_pal and isPalindrome(str(prod)):
			largest_pal = prod
print(largest_pal)