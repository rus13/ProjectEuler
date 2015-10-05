__author__ = 'ruslan'

from math import factorial

fac = {}
for i in range(10):
    fac[i] = factorial(i)
d_fact = 0
for n in range(3, 10**7):
    res = 0
    for i in str(n):
        res += fac[int(i)]
    if n == res:
        d_fact += n
print(d_fact)