#assume n is never negative
def fibonacci(n, dict):
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
    if n == 0 or n == 1:
        return 1
    return fibonacci(n-1, dict) + fibonacci(n-2, dict)

def fibonacciMemo(n, dict, memo):
    if n in memo:
        return memo[n]
    if n in dict:
        dict[n] += 1
    else:
        dict[n] = 1
    if n == 0 or n == 1:
        return 1
    current_n = fibonacciMemo(n-1, dict, memo) + fibonacciMemo(n-2, dict, memo)
    memo[n] = current_n
    return current_n


def fibonacciBottomUp(n):
    dp = [0]*(n+1)
    dp[0] = dp[1] = 1
    count = 2
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        count += 1
    print("fibonacciBottomUp count: " + str(count))
    return dp[-1]





if __name__ == '__main__':
    #test cases

    #0   ...   11
    #1,1,2,3,5,8,13,21,34,55,89,144


    #f(n) = f(n-1) + f(n-2)
    #n = 0    -> 1
    #n = 1    -> 1
    #n = 2    -> 2
    #n = 3    -> 3
    #n = 4    -> 5

    fibonacciDict = {}
    fibonacciMemoDict = {}
    memo = {}
                            # 7
                        #   6   5
                        # 4  5 3 4
    n = 20
    print(fibonacci(n, fibonacciDict))
    stack_calls = sum(fibonacciDict.values())
    print("stack calls fibonacci no memo ", stack_calls)


    print(fibonacciMemo(n, fibonacciMemoDict, memo))
    stack_calls = sum(fibonacciMemoDict.values())
    print("stack calls fibonacci", stack_calls)

    print(fibonacciBottomUp(n))
