#Project Euler Problem 2: p2.py
sum = 0
last = 1
cur = 1
temp = 0

while cur <= 4000000:
	if cur % 2 == 0:
		sum = sum + cur
	temp = cur
	cur = cur + last
	last = temp
print(sum)
