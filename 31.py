__author__ = 'Ruslan'

val = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [1] + ([0]*val)
for coin in coins:
    for j in range(coin, val+1):
        dp[j] += dp[j-coin]
print(dp[val])