obstacleGrid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
n = len(obstacleGrid) - 1
m = len(obstacleGrid[0]) - 1
dp = []

# Trace DP initial
# Code
if obstacleGrid[n][m] != 1:
  dp[n][m] = 1
# DP so far from initial bit
[
  [0, 0, 0], 
  [0, 0, 0], 
  [0, 0, 1]
]


# Trace DP 1st pre-processing
# Code
for i in range(n-1,-1,-1):
  if obstacleGrid[i][m] != 1:
    dp[i][m] = dp[i+1][m]

# Trace
dp[1][2] = dp[2][2]
0 = 1

dp[0][2] = dp[1][2]
0 = 1

# DP so far
[
  [0, 0, 1], 
  [0, 0, 1], 
  [0, 0, 1]
]


## Trace DP 2nd pre-processing
# Code
for j in range(m-1,-1,-1):
  if obstacleGrid[n][j] != 1:
    dp[n][j] = dp[n][j + 1] 

# Trace
dp[2][1] = dp[2][2]
0 = 1

dp[2][0] = dp[2][1]
0 = 1

# DP so far
[
  [0, 0, 1], 
  [0, 0, 1], 
  [1, 1, 1]
]


# Trace core DP
# Code
for i in range(n-1, -1, - 1):
  for j in range(m-1, -1, -1):
    if obstacleGrid[i][j] != 1:
      dp[i][j] = dp[i+1][j] + dp[i][j+1]

# Trace
dp[1][0] = dp[2][0] + dp[1][1]
0 = 1 + 0

dp[0][1] = dp[1][1] + dp[0][2]
0 = 0 + 1

dp[0][0] = dp[1][0] + dp[0][1]
0 = 1 + 1

# Final DP
[
  [2, 1, 1], 
  [1, 0, 1], 
  [1, 1, 1]
]
