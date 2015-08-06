__author__ = 'Ruslan'

from lib.sieve import sieve
primes = sieve(1000000)
b_range = sieve(1000)
a_best = -1000
b_best = -1000
max_prime = 0
for b in b_range:
    for a in [p-b-1 for p in b_range]:
        n = 1
        while (n*n + a*n + b) in primes:
            n += 1
        if n > max_prime:
            max_prime = n
            a_best = a
            b_best = b
print(a_best * b_best)