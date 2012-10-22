#Project Euler p17.py

#define all string used as building blocks
d = {}
d.update({1: len('one')})
d.update({2: len('two')})
d.update({3: len('three')})
d.update({4: len('four')})
d.update({5: len('five')})
d.update({6: len('six')})
d.update({7: len('seven')})
d.update({8: len('eight')})
d.update({9: len('nine')})
d.update({10: len('ten')})
d.update({11: len('eleven')})
d.update({12: len('twelve')})
d.update({13: len('thirteen')})
d.update({14: 4+d[4]})
d.update({15: len('fifteen')})
d.update({16: 4+d[6]})
d.update({17: 4+d[7]})
d.update({18: len('eighteen')})
d.update({19: 4+d[9]})
d.update({20: len('twenty')})
d.update({30: len('thirty')})
d.update({40: len('forty')})
d.update({50: len('fifty')})
d.update({60: len('sixty')})
d.update({70: len('seventy')})
d.update({80: len('eighty')})
d.update({90: len('ninety')})
h = len('hundred')
d.update({1000: len('onethousand')})

#now do hundreds
for i in range(1,10):
	d.update({100*i: h+d[i]})

#everything else we can can in reference to above defined
def letters(x):
	if x <= 19:
		return d[x]
	if x >= 20 and x <= 99:
		tens = (x/10)*10 #concats since its ints
		ones = x%10
		onesEntry = (d[ones] if ones != 0 else 0)
		return d[tens]+onesEntry
	if x >= 100 and x <= 999:
		huns = (x/100)*100
		rest = x%100
		andEntry = (len('and') + letters(rest) if rest != 0 else 0)
		return d[huns]+andEntry
	else: return d[1000]

#run that shit
count = 0
for i in range(1, 1001):
	count += letters(i)
print(count)

