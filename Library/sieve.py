__author__ = 'Ruslan'
from math import sqrt, floor


def sieve(n):
    if n < 2:
        return []
    bound = int((n - 1) / 2)
    a = [True for i in range(0, bound + 1)]
    a[0] = False
    limit = int((floor(sqrt(n)) - 1) / 2)
    for i in range(limit + 1):
        if a[i]:
            for k in range(2 * i * (i + 1), bound, 2 * i + 1):
                a[k] = False
    p = [2]
    for i in range(len(a)):
        if a[i]:
            p.append(2 * i + 1)
    return p