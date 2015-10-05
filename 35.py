__author__ = 'ruslan'

from lib.sieve import sieve
from re import match

prim = [p for p in sieve(1000000) if not match('[2468]', str(p))]
prim = set(prim)
found = []
for p in prim:
    s = str(p)
    circ_prime = True
    for i in range(len(s)-1):
        s = s[1:] + s[0]
        if int(s) not in prim:
            circ_prime = False
            break
    if circ_prime:
        found.append(p)
print(len(found))