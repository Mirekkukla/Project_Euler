from math import *
max_sols = 0
best_p = 0
# the shortest side can be no larger than 'a' where
# a^2 + a^2 = req_primes^2 and a + a + req_primes = p
# solving gives a = .5(2p - sqrt(2)*p)

for p in range(1, 1001):
    max_pos_shortest = floor(.5*(2*p - sqrt(2)*p))
    sols = 0
    for a in range(1, max_pos_shortest + 1): #the shortest side
        b = p*(2*a-p)/(2*(a-p))
        req_primes = -(2*pow(a,2)-2*a*p+pow(p,2))/(2*a-2*p)
        if pow(int(a),2) + pow(int(b),2) == pow(int(req_primes),2):
            sols += 1
    if sols > max_sols:
        max_sols = sols
        best_p = p
print(best_p)
print(max_sols)