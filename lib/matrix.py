__author__ = 'Ruslan'
import time


def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1
    a = [[0, 1], [1, 1]]
    return power(a, n - 1)[1][1]


def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    f1 = 0
    f2 = 1
    for i in range(n-1):
        f1, f2 = f2, f1+f2
    return f2


def power(a, n):
    b = "{0:b}".format(n)
    d = [[0]*len(a)]*len(a)
    for i in range(len(a)):
        d[i][i] = 1
    for i in b:
        d = mult(d,d)
        if i == '1':
            d = mult(d,a)
    return d


def mult(a,b):
    c = [[0 for i in range(len(a))] for j in range(len(b[0]))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                c[i][j] += a[i][k]*b[k][j]
    return c

t1 = time.time()
print(fibonacci(800000))
#print(fib(1000000))
t2 = time.time()
print(t2-t1)