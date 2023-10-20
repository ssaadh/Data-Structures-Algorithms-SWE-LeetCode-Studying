class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        memo = [[-1]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        return self._uniquePaths(obstacleGrid, 0, 0, memo)

    def _uniquePaths(self,obstacleGrid,i,j, memo):
        if i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
            return 1

        if memo[i][j] != -1:
            return memo[i][j]

        count = 0
        directions = ((1,0), (0,1))
        for x,y in directions:
            x,y = x + i, y + j
            if 0 <= x < len(obstacleGrid) and 0 <= y < len(obstacleGrid[0]) and obstacleGrid[x][y] != 1:
                count += self._uniquePaths(obstacleGrid, x, y, memo)

        memo[i][j] = count
        return count
