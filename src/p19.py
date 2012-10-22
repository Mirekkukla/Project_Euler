#Project Euler prob 19: p19.py
firstMSundays = 0
year = 1901
month = 1
day = 0 
dayOfWeek = 0

def isLeapYear(x):
	if x % 400 == 0: return True
	elif x % 100 == 0: return False
	elif x % 4 == 0: return True
	else: return False

while year <= 2000 and month <= 12 and day <= 31:
	if dayOfWeek == 6 and day == 1: firstMSundays += 1
	if month == 2 and isLeapYear(year):
		if day == 29:
			day = 1
			dayOfWeek = (dayOfWeek + 1)%7
			month += 1
		else:
			day += 1
			dayOfWeek = (dayOfWeek + 1)%7
	elif month == 2 and not isLeapYear(year):
		if day == 28:
			day = 1
			dayOfWeek = (dayOfWeek + 1)%7
			month += 1
		else:
			day += 1
			dayOfWeek = (dayOfWeek + 1)%7
	elif month == 4 or month == 6 or month == 9 or month == 11:
		if day == 30:
			day = 1
			dayOfWeek = (dayOfWeek + 1)%7
			month += 1
		else:
			day += 1
			dayOfWeek = (dayOfWeek + 1)%7
	else:
		if day == 31:
			day = 1
			dayOfWeek = (dayOfWeek + 1)%7
			if month == 12:
				month = 1
				year += 1
			else:
				month += 1
		else:
			day += 1
			dayOfWeek = (dayOfWeek + 1)%7
print(firstMSundays)
