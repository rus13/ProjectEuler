__author__ = 'ruslan'

from lib.sieve import sieve

prime = sieve(1000000)
is_prime = set(prime)
trunc = []
i = 4
while len(trunc) < 11:
    p = str(prime[i])
    tr = True
    for k in range(1, len(p)):
        if int(p[k:]) not in is_prime or int(p[:-k]) not in is_prime:
            tr = False
            break
    if tr:
        trunc.append(int(p))
    i += 1
print(sum(trunc))