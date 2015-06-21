__author__ = 'Ruslan'
from math import sqrt,ceil

p = []
limit = 100001
a = []
for i in range(1000000):
    a.append(True)
for i in range(2,len(a)):
    if a[i]:
        p.append(i)
        tmp = 1
        while tmp * i < len(a):
            a[tmp * i] = False
            tmp += 1
print(p[10000])