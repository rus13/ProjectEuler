__author__ = 'Ruslan'
from time import time
import operator

# def get(n):
#     start = n
#     count = 0
#     while n >= len(dp) or dp[n] == 0:
#         count += 1
#         if n % 2 == 0:
#             n //= 2
#         else:
#             n = 3*n + 1
#
#     if (start < len(dp)) and (dp[start] == 0):
#         dp[start] = dp[n]+count
#     return dp[start]


cache = {1: 1}
t1 = time()
for i in range(2,1000000):
    n = i
    li = [n]
    while n not in cache:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3*n + 1
        li.append(n)
    li.reverse()
    for j in range(1, len(li)):
        cache[li[j]] = cache[n] + j
m = max(cache, key=cache.get)
print(m)
print(time()-t1)