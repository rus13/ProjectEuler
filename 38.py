__author__ = 'ruslan'

# only 4 digit numbers in range 9182-9999 are greater than the example
for i in range(9999, 9182, -1):
    pan = str(i) + str(i*2)
    if len(pan)==9 and sorted(pan) == list('123456789'):
        print(pan)
        break