import functions.primes
s = set()
n = 100

for a in range(2,n + 1):
    for b in range(2,n + 1):
        initial_factorization = functions.primes.primeFactorization(a)
        final_factorization = initial_factorization
        for i in range (0,b - 1):
            final_factorization += initial_factorization
        factor_list = list(final_factorization.elements())
        factor_list.sort(key=int)
        s.add(tuple(factor_list))
print(len(s))