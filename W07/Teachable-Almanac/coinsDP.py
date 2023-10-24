class Solution:
  # recurrence relation:
  # dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i]]+1)
  def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]
    dp[0][0] = 0
    firstCoin = coins[0]
    for i in range(amount + 1):
      if i >= firstCoin:
        dp[0][i] = dp[0][i - firstCoin] + 1    
    # At this point, dp is:
    # [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]]

    for i in range(1, len(coins)):
      for j in range(amount + 1):
        coinValue = coins[i]
        if j >= coinValue:
          dp[i][j] = min(dp[i - 1][j], dp[i][j - coinValue] + 1)
        else:
          dp[i][j] = dp[i - 1][j]

    if dp[-1][-1] != float('inf'):
      return dp[-1][-1]
    else:
      return -1

  def coinChangePrinting(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    dp = [[float('inf')] * (amount + 1) for _ in range(len(coins))]
    dp[0][0] = 0
    firstCoin = coins[0]
    # print('firstCoin', firstCoin)
    for i in range(amount + 1):
      # print('i', i)
      if i >= firstCoin:
        # print('minus', i-firstCoin)
        dp[0][i] = dp[0][i - firstCoin] + 1
    
    # At this point, dp is:
    # [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf], [inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]]
    # print(dp)
    count = 0
    for i in range(1, len(coins)):
      for j in range(amount + 1):
        count += 1
        coinValue = coins[i]
        if j >= coinValue:
          # print('first', i, j, coinValue)
          # print(dp[i - 1][j], dp[i][j - coinValue] + 1)
          print(f"dp[{i}][{j}] = min(dp[{i - 1}][{j}], dp[{i}][{j - coinValue}] + 1)")
          print(f"{dp[i][j]} = min({dp[i - 1][j]}, {dp[i][j - coinValue] + 1})")
          dp[i][j] = min(dp[i - 1][j], dp[i][j - coinValue] + 1)
        else:
          print(f"dp[{i}][{j}] = dp[{i - 1}][{j}]")
          print(f"{dp[i][j]} = {dp[i - 1][j]}")
          # print('second', i, j, coinValue)
          # print(dp[i - 1][j])
          dp[i][j] = dp[i - 1][j]

    print(count)
    if dp[-1][-1] != float('inf'):
      return dp[-1][-1]
    else:
      return -1


  ##
  # Brute force with Memo
  ##
  def coinChangeMemo(self, coins, amount):
    self.minCoins = float('inf')
    memo = [float('inf')] * amount
    self.bruteForceSearchMemo(coins, 0, 0, amount, memo)
    if self.minCoins == float('inf'):
      return -1
    return self.minCoins
  
  def bruteForceSearchMemo(self, coins, curAmount, numCoins, target, memo):
    if curAmount >= target:
      if curAmount == target:
        self.minCoins = min(self.minCoins, numCoins)
        return numCoins
      return float('inf')
    if memo[curAmount] <= numCoins:
      return memo[curAmount]
    smallest = float('inf')
    for coin in coins:
      smallest = min(smallest, self.bruteForceSearchMemo(coins, curAmount + coin, numCoins + 1, target, memo))
    memo[curAmount] = smallest
    return smallest
  

  ##
  # Brute force Without optimization
  ##
  def coinChangeNormal(self, coins, amount):
    self.minCoins = float('inf')
    self.bruteForceSearchNormal(coins, 0, 0, amount)
    if self.minCoins == float('inf'):
      return -1
    return self.minCoins
  
  def bruteForceSearchNormal(self, coins, curAmount, numCoins, target):
    if curAmount >= target:
      if curAmount == target:
        self.minCoins = min(self.minCoins, numCoins)
      return
    for coin in coins:
      self.bruteForceSearchNormal(coins, curAmount + coin, numCoins + 1, target)

# s = Solution()
# print(s.coinChangePrinting([1, 2, 5], 11))
# print(s.coinChangeMemo([1, 2, 5], 11))
