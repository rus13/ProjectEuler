__author__ = 'ruslan'


def palindrom(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


s = 0
for n in range(1000000):
    b10 = str(n)
    b2 = "{0:b}".format(n)
    if palindrom(b10) and palindrom(b2):
        s += n
print(s)