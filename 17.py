num_dict = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
        9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety", 100: "hundred",
        1000: "thousand"}


def num_to_string(num):
    string = ""
    if num < 20:
        string = num_dict[num]
    elif num < 100:
        if num % 10 == 0:
            string = num_dict[(num // 10) * 10]
        else:
            string = num_dict[(num // 10) * 10] + "-" + num_dict[num % 10]
    else:
        s = str(num)
        first = int(s[0])
        rest = int(s[1:])
        string += num_dict[first] + " " + num_dict[10 ** (len(s) - 1)]
        if rest > 0:
            if rest < 100:
                string += " and"
            string += " " + num_to_string(rest)
    return string


count = 0
for i in range(0, 1001):
    s = num_to_string(i)
    print(s)
    s = s.replace(' ', '')
    s = s.replace('-', '')
    count += len(s)
print(count)
