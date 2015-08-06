from time import time

__author__ = 'Ruslan'


def c_len(n):
    rem = 1
    cycle = [1]
    while True:
        rem = (rem * 10) % n
        if rem == 0:
            return 0
        if cycle.count(rem) > 0:
            ind = cycle.index(rem)
            return sum(len(str(i)) for i in range(ind,len(cycle)) )
        cycle.append(rem)

t = time()
max_c = 0
max_i = 2
for i in range(1000, 1, -1):
    cur_c = c_len(i)
    if cur_c > max_c:
        max_c = cur_c
        max_i = i
print(max_i)
print(time()-t)