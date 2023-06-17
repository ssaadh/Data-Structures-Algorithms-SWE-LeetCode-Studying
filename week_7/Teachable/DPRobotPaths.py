class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
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
