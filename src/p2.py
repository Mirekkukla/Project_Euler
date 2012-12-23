#Project Euler Problem 2: p2.py
even_fib_sum = 0
last_fib = 1
cur_fib = 1

while cur_fib <= 4000000:
	if cur_fib % 2 == 0:
		even_fib_sum += cur_fib
	cur_fib_copy = cur_fib
	cur_fib = cur_fib + last_fib
	last_fib = cur_fib_copy

print(even_fib_sum)
