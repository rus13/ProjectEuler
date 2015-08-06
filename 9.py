__author__ = 'Ruslan'
tmp = 0
for a in range(1,1000):
    for b in range(a+1,1000):
        c = 1000 - a - b
        if (a < b) & (b < c) & ((a ** 2) + (b ** 2) == c ** 2):
            print(a*b*c)