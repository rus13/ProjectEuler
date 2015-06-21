__author__ = 'Ruslan'

# r = 1001
# s = 1
# for n in range(3, r+1, 2):
#     s += 4*n*n - 6*(n-1)

print(sum([4*n*n - 6*(n-1) for n in range(3, 1001+1, 2)])+1)