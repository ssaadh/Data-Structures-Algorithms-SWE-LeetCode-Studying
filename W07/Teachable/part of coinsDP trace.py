part of coinsDP trace:

dp = []
coins = [1, 2, 5]
amount = 11

# coin 1 is already done before

for i in range(1, len(coins)):
  for j in range(amount + 1):
    coinValue = coins[i]
    if j >= coinValue:
      dp[i][j] = min(dp[i - 1][j], dp[i][j - coinValue] + 1)
    else:
      dp[i][j] = dp[i - 1][j]


## Trace

# Each line is doing either:
dp[i][j] = min(dp[i - 1][j], dp[i][j - coinValue] + 1)
# OR
dp[i][j] = dp[i - 1][j]
# First trace line is showing how it looks with all variables filled in
# Second trace line is showing the value of the variables

# first loop. i = 1, coinValue = 2

# j < coinValue
# j < 2
dp[1][0] = dp[0][0]
inf = 0

dp[1][1] = dp[0][1]
inf = 1

# j >= coinValue
# j >= 2
dp[1][2] = min(dp[0][2], dp[1][0] + 1)
inf = min(2, 1)

dp[1][3] = min(dp[0][3], dp[1][1] + 1)
inf = min(3, 2)

dp[1][4] = min(dp[0][4], dp[1][2] + 1)
inf = min(4, 2)

dp[1][5] = min(dp[0][5], dp[1][3] + 1)
inf = min(5, 3)

dp[1][6] = min(dp[0][6], dp[1][4] + 1)
inf = min(6, 3)

dp[1][7] = min(dp[0][7], dp[1][5] + 1)
inf = min(7, 4)

dp[1][8] = min(dp[0][8], dp[1][6] + 1)
inf = min(8, 4)

dp[1][9] = min(dp[0][9], dp[1][7] + 1)
inf = min(9, 5)

dp[1][10] = min(dp[0][10], dp[1][8] + 1)
inf = min(10, 5)

dp[1][11] = min(dp[0][11], dp[1][9] + 1)
inf = min(11, 6)


## i iterates. 2nd/last loop of i = 2, coinValue = 5

# j < coinValue
# j < 5
dp[2][0] = dp[1][0]
inf = 0

dp[2][1] = dp[1][1]
inf = 1

dp[2][2] = dp[1][2]
inf = 1

dp[2][3] = dp[1][3]
inf = 2

dp[2][4] = dp[1][4]
inf = 2

# j >= coinValue
# j >= 5
dp[2][5] = min(dp[1][5], dp[2][0] + 1)
inf = min(3, 1)

dp[2][6] = min(dp[1][6], dp[2][1] + 1)
inf = min(3, 2)

dp[2][7] = min(dp[1][7], dp[2][2] + 1)
inf = min(4, 2)

dp[2][8] = min(dp[1][8], dp[2][3] + 1)
inf = min(4, 3)

dp[2][9] = min(dp[1][9], dp[2][4] + 1)
inf = min(5, 3)

dp[2][10] = min(dp[1][10], dp[2][5] + 1)
inf = min(5, 2)

dp[2][11] = min(dp[1][11], dp[2][6] + 1)
inf = min(6, 3)
