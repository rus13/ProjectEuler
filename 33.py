__author__ = 'ruslan'
from functools import reduce
from fractions import Fraction
from operator import mul

found = set()
for i in range(1,10):
    for j in range(i+1, 10):
        for x in range(1,10):
            f = Fraction(i, j)
            if f == Fraction(x * 10 + i, j * 10 + x) or f == Fraction(i * 10 + x, x * 10 + j):
                found.add(f)
print(reduce(mul,found))