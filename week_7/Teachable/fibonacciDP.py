def fibonacci(n):
    if n == 0:
        return 0
    dp = [0]*(n+1)
    dp[1] = 1

    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]




if __name__ == '__main__':
    #0,1,1,2,3,5,8,13,21,34, 55
    #0,1,2,3,4,5,6,7, 8, 9,  10

    #f(n) = f(n-1) + f(n-2)
    #dp[n] = dp[n-1] + dp[n-2]
    #dp[0] = 0
    #dp[1] = 1

    for n in range(11):
        print(fibonacci(n))
