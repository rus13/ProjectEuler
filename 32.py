__author__ = 'Ruslan'

from itertools import permutations,combinations

found = set()
for p in permutations("123456789"):
    for c in combinations(range(1,9), 2):
        i, j = c
        multiplicand = int(''.join(p[:i]))
        multiplier = int(''.join(p[i:j]))
        product = int(''.join(p[j:]))
        if multiplicand * multiplier == product:
            found.add(product)
print(sum(found))