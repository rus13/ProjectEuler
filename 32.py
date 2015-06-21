__author__ = 'Ruslan'


def isPand(l):
    if len(l) != 9:
        return False;
    else:
        count = [False]*9
        for i in l:
            if count[i]:
                return False
            count[i] = True


s = 0

for i in range(10, 999):
    for j in range(10,999):
        mult = i*j
        l = str