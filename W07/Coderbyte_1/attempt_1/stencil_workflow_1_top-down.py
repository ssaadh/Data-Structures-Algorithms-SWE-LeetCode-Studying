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
Question 1. Solve the above problem using Top Down Dynamic Programming
'''

# brute force recursion
# no optimization
# Time, Space: O(n^2) at least
def unique_paths_top_down_bf(m: int, n: int) -> int:
  def _helper(m, n, i, j):
    # m - 1 and n - 1 -> return 1
    # m + 1 or n + 1 -> return 0, off the board
    if i == m or j == n:
      return 0
    elif i == m - 1 and j == n - 1:
      return 1
    else:
      return _helper(m - 1, n, i, j) + _helper(m, n - 1, i, j)
    
  return _helper(m, n, 0, 0)

# Adding memo. Using dict because comfy with it.
# Time: O(m * n)
# Space: O(m * n) for the memo and O(m * n) in memory stack
def unique_paths_top_down(m: int, n: int) -> int:
  def _helper(m: int, n: int, memo: dict) -> int:
    # if m, n in memo, return memo(m, n)
    if (m, n) in memo:
        return memo[(m, n)]
    # m - 1 and n - 1 -> return 1
    if m < 0 or n < 0:
        memo[(m, n)] = 0
    # m + 1 or n + 1 -> return 0, off the board
    elif m == 0 and n == 0:
        memo[(m, n)] = 1
    else:
        # return grid(m - 1, n) + grid(m, n - 1)
        memo[(m, n)] = _helper(m - 1, n, memo) + _helper(m, n - 1, memo)
    return memo[(m, n)]
  
  memo = dict()
  return _helper(m - 1, n - 1, memo)
