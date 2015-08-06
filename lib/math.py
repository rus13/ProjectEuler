__author__ = 'Ruslan'
from math import sqrt,pi,e


def stirling(n):
    return sqrt(2*pi*n)*(n/e)**n


def binomial(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)
    res = 1
    for i in range(k):
        res = res * (n - i) // (i + 1)
    return res
