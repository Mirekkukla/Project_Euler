#Project Euler prob 4: p4.py

def isPalindrome(n):
	s = str(n)
	for i in range(int(len(s)/2)):
		if s[i] != s[-(i + 1)]:
			return False
	return True

def doit():	
	totalBreak = False
	for i in reversed(range(100*100, 999*999+1)):
		if totalBreak:
			break
		if isPalindrome(i):
			for j in reversed(range(100,999)):
				if (i % j == 0) and (len(str(i/j)) == 3):
					print(i)
					totalBreak = True
					break
				if i/j > 999:
					break
