__author__ = 'ruslan'

from math import sqrt, floor
from time import time

def egcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q, y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    gcd = b
    return gcd, x, y


# naive approach
# start = time()
# p = [0]*1000
# for a in range(1, 500):
#     for b in range(a, 500):
#         c = sqrt(a**2 + b**2)
#         if c == floor(c) and a + b + c <= 1000:
#             p[a+b+int(c) - 1] += 1
# print(max(enumerate(p), key=lambda p:p[1])[0]+1)
# print(time() - start)


# generate all primitive Pythagorean triples (x, y, z) with z < 1000
# also generate the non-primitive triples from the primitive via multiplication with a variable
start = time()
p = [0]*1001
for u in range(32):
    for v in range(1, u):
        if egcd(u, v)[0] == 1:
            x = u**2 - v**2
            y = 2*u*v
            z = u**2 + v**2
            n = 1
            while x*n + y*n + z*n <= 1000:
                p[x*n + y*n + z*n] += 1
                n += 1

print(max(enumerate(p), key=lambda p:p[1])[0])
print(time() - start)