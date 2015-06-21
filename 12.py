__author__ = 'Ruslan'

found = False
n = 1
while not found:
    count = 2
    number = int((n * (n + 1)) / 2)
    stop = number
    div = 2
    while div < stop:
        if number % div == 0:
            count += 2
            stop = min(stop, int(number / div))
        div += 1
    # if count > 300:
    #     print("number:", number, "count:", count, sep=" ")
    if count >= 500:
        print("number:", number, "count:", count, sep=" ")
        found = True
    # print("number:", number, "count:", count, sep=" ")
    n += 1