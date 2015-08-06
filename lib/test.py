from Library.math import binomial
from Library.sieve import sieve
from Library.algorithm import quicksort_iterative
from Library.algorithm import mergesort_iterative
from random import random
from math import floor
__author__ = 'Ruslan'

import Library.math
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

t1 = time.time()
numbers = 1000
array = []
for i in range(numbers):
    array.append(floor(random()*numbers))
mergesort_iterative(array)
t2 = time.time()
print(t2 - t1)
print(array)