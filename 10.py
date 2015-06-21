__author__ = 'Ruslan'
from math import sqrt,ceil
from Library.sieve import sieve
p = sieve(20000000)
s = 0
for i in range(len(p)):
    s += p[i]
print(s)