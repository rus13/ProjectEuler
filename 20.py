__author__ = 'Ruslan'
import math

f = math.factorial(100)
s = str(f)
sum = 0
for i in range(len(s)):
    sum += int(s[i])
print(sum)