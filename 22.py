__author__ = 'Ruslan'
import string


f = open('p022_names.txt', 'r')
s = f.read().replace('"', '').split(',')
s.sort()
score = [0]*len(s)
for i in range(len(s)):
    worth = 0
    for j in s[i]:
        worth += string.ascii_lowercase.index(j.lower()) + 1
    score[i] = worth * (i+1)
print(sum(score))