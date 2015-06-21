__author__ = 'Ruslan'
import math
abundant = []
for num in range(28124):
    div = set()
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            div.add(i)
            div.add(num/i)
    if sum(div) > num:
        abundant.append(num)
r = set(range(28124))
for i in abundant:
    for j in abundant:
        r.discard(i+j)
print(sum(r))