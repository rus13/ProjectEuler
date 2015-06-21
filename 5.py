__author__ = 'Ruslan'
import math


def pal(n):
    st = str(n)
    pal = True
    for i in range(len(st)):
        if st[i] != st[-i - 1]:
            pal = False
            break
    return pal


def ggt(l):
    e = 0;
    for x in l:
        e = euclid(e, x)
    return e


def euclid(a, b):
    if a == 0: return b
    if b == 0: return a
    return euclid(b, a % b)


def div(a):
    for i in range(2,21):
        if a % i != 0:
            return False
    return True


x = math.factorial(20)

# m=ggt(list(range(1,21)))
tmp = 1
for i in range(1, x, 1):
    if div(i):
        tmp = i
        break
print(tmp)