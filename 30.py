from time import time

__author__ = 'ruslan'

now = time()
sp = 0
for i in range(2, 1000000):
    s = str(i)
    if i == sum(int(s[j])**5 for j in range(0,len(s))):
        sp += i
print(sp)
print((time()-now))