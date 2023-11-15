from __future__ import annotations

'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

'''
Question 2. Solve the above problem using Bottom Up Dynamic Programming
'''

# 0, 0
# [1, 1,  1,  1,  1]
# [1, 2,  3,  4,  5]
# [1, 3,  6, 10, 15]
# [1, 4, 10, 20, 35]

# Start at 1st index so can add from the 0 index first column.
# The first column and row so the top row and most left column are all 1. There is just 1 way to get to them. You can only go down or right.

def unique_paths_bottom_up_dp(m: int, n: int) -> int:
  dp = [[1 if i == 0 or j == 0 else 0 for i in range(m)] for j in range(n)]

  for i in range(1, n):
    for j in range(1, m):
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1] 

  return dp[-1][-1]

# The amt of columns is what we care about. We need just the current row and all the columns for that row to compute the dp
# Doing the tabulation shows that the math is very simple. It's adding the current number with the previous number.
# Like after doing [1, 1, 1, 1, 1], for range(1, len), the current var plus the previous var is the answer so:
# [1, 2 (1 + 1), 3 (2 + 1), 4 (3 + 1), 5 ( 4 + 1)]
# To break it down even further each of the inner loops would do this:
# [1, 1, 1, 1, 1]
# [1, 2, 1, 1, 1]
# [1, 2, 3, 1, 1]
# [1, 2, 3, 4, 1]
# [1, 2, 3, 4, 5]
# Now one inner loop is completely done.
def unique_paths_bottom_up(m: int, n: int) -> int:
  cur = [1] * n
  for _ in range(1, m):
    for col in range(1, n):
      cur[col] += cur[col - 1]
    print(cur)
  return cur[-1]

# print(unique_paths_bottom_up(2, 2))
print(unique_paths_bottom_up(5, 4))
# print(uniquePaths(3, 3))


[1, 1, 1, 1, 1]
[1, 2, 3, 4, 5]
[1, 3, 6, 10, 15]
