__author__ = 'Ruslan'

import string

s = string.ascii_lowercase

def num_to_string(num):
    s = str(num)[::-1]
    string = []
    if len(s) == 1:
        string.append(dict[num])
    elif num < 20:
        string.append(dict[num])
        if num > 1:
                if num%10 != 0:
                    string.append(dict[num%10]+"-" + dict[(num//10)%10])
                else:
                    string.append(dict[num%10])
            else:
                string.append(dict[])
            if num//10 > 0 and len(string)>0:
                string.append("and")

    for i in range(0, len(s), 1):
        cur = num%10
        if i == 0:
            string.append(dict[cur])
        elif i == 1:
            prev = string.pop()
            if cur > 1:
                if prev != dict[0]:
                    string.append(dict[cur]+"-" + prev)
                else:
                    string.append(dict[cur])
            else:
                string.append(dict[])
            if num//10 > 0 and len(string)>0:
                string.append("and")
        elif i == 2 and cur != 0:
            string.append(dict[100])
            string.append(dict[cur])
        elif i == 3 and cur != 0:
            string.append(dict[1000])
            string.append(dict[cur])
        num //= 10
    return " ".join(string[::-1])