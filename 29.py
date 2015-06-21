__author__ = 'Ruslan'
dict = {}
for a in range(2,101):
    for b in range(2,101):
        val = a**b
        dict[val] = val
print(len(dict))