__author__ = 'Ruslan'

f = open('input17.txt')
data = []
for line in f:
    l = line.split()
    data.append([int(i) for i in l])

dp = [[data[0][0]]]
for i in range(1, len(data)):
    l = len(data[i])
    dp.append([0 for k in range(l)])
    for j in range(l):
        if j > 0:
            dp[i][j] = max(dp[i][j], dp[i-1][j-1] + data[i][j])
        if j < l - 1:
            dp[i][j] = max(dp[i][j], dp[i-1][j] + data[i][j])

print(max(dp[len(dp)-1]))