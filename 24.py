__author__ = 'Ruslan'
import itertools

ord = 1000000 - 1
perm = list(itertools.permutations(range(10)))
x = [str(i) for i in perm[ord]]
print(''.join(x))

