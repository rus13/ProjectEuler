__author__ = 'Ruslan'
import math
n = 20
dp = [[0]*(n+1) for i in range(n+1)]
# for i in range(n+1):
#     dp[0][i] = dp[i][0] = 1
for i in range(n+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
print(dp[n][n])

# print(math.factorial(2*n)//(math.factorial(n)**2))
