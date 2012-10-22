#project Euler prob 7: p7/py
primes = []
i = 2
while True:
	isPrime = True
	for j in range(len(primes)):
		if i % primes[j] == 0:
			isPrime = False
			break
	if isPrime:
		primes.append(i)
	if len(primes) == 10001:
		break
	i += 1
print(primes[-1])
