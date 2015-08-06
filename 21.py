from math import sqrt


def d(a):
    s = 0
    for i in range(1, a):
        if a % i == 0:
            s += i
    return s


s = 0
for a in range (2, 10000):
    b = d(a)
    if b > a and d(b) == a:
        s += a + b
print(s)