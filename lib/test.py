from lib.sort import quicksort_iterative,quicksort_recursive,mergesort_iterative,mergesort_recursive
from random import random
from math import floor
import time

# t1 = time.time()
# for i in range(10000000):
#     s = "{0:b}".format(i)
# t2 = time.time()
# print(t2 - t1)

# t1 = time.time()
# for i in range(1000000):
#     s = []
#     while i//2 > 0:
#         s.append(i % 2)
#         i //= 2
#     s.reverse()
# t2 = time.time()
# print(t2 - t1)

numbers = 1000000
array = []
for i in range(numbers):
    array.append(floor(random()*numbers))
t1 = time.time()
tmp = list(array)
mergesort_recursive(tmp,0,len(array))
t2 = time.time()
print(t2 - t1)
#print(tmp)
tmp = list(array)
t1 = time.time()
mergesort_iterative(tmp,0,len(array))
t2 = time.time()
print(t2 - t1)
#print(tmp)
tmp = list(array)
t1 = time.time()
sorted(tmp)
t2 = time.time()
print(t2 - t1)