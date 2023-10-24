class Solution:
  def uniquePathsWithObstacles(self, obstacleGrid) -> int:
    if not obstacleGrid:
      return 0
    dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    n = len(obstacleGrid) - 1
    m = len(obstacleGrid[0]) - 1
    if obstacleGrid[n][m] != 1:
      dp[n][m] = 1

    for i in range(n-1,-1,-1):
      if obstacleGrid[i][m] != 1:
        dp[i][m] = dp[i+1][m]
    for j in range(m-1,-1,-1):
      if obstacleGrid[n][j] != 1:
        dp[n][j] = dp[n][j + 1] 

    for i in range(n-1, -1, - 1):
      for j in range(m-1, -1, -1):
        if obstacleGrid[i][j] != 1:
          dp[i][j] = dp[i+1][j] + dp[i][j+1]

    return dp[0][0]

  def uniquePathsPrint(self, obstacleGrid) -> int:
    if not obstacleGrid:
      return 0
    dp = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
    n = len(obstacleGrid) - 1
    m = len(obstacleGrid[0]) - 1
    if obstacleGrid[n][m] != 1:
      dp[n][m] = 1

    for i in range(n-1,-1,-1):
      if obstacleGrid[i][m] != 1:
        print(f"dp[{i}][{m}] = dp[{i + 1}][{m}]")
        print(f"{dp[i][m]} = {dp[i + 1][m]}")
        dp[i][m] = dp[i+1][m]
    print(dp)

    for j in range(m-1,-1,-1):
      if obstacleGrid[n][j] != 1:
        print(f"dp[{n}][{j}] = dp[{n}][{j + 1}]")
        print(f"{dp[n][j]} = {dp[n][j + 1]}")
        dp[n][j] = dp[n][j + 1] 
    print(dp)

    for i in range(n-1, -1, - 1):
      for j in range(m-1, -1, -1):
        if obstacleGrid[i][j] != 1:
          print(f"dp[{i}][{j}] = dp[{i + 1}][{j}] + dp[{i}][{j + 1}]")
          print(f"{dp[i][j]} = {dp[i + 1][j]} + {dp[i][j + 1]}")
          dp[i][j] = dp[i+1][j] + dp[i][j+1]
    print(dp)
    return dp[0][0]

# s = Solution()
# grid = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
# print(s.uniquePathsPrint(grid))
# print(s.coinChangePrinting([1, 2, 5], 11))
# print(s.coinChangeMemo([1, 2, 5], 11))
