__author__ = 'Ruslan'
import math

s = 0
for i in range(101):
    s += i**2
t = 101*100/2
t = t**2
print(t-s)