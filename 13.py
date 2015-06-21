__author__ = 'Ruslan'

f = open('input13.txt', 'r')
# sum = 0
# for line in f:
#     sum += int(line)
# print(str(sum)[0:10])
print(str(sum(map(int,f.read().split("\n"))))[0:10])