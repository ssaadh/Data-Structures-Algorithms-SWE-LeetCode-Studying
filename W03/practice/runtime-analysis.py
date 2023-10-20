def fn_g(n: int, m: int) -> int:
  if n <= 0 or m <= 0:
    return 1
  return fn_g(n//2, m) + fn_g(n, m//2)

print(fn_g(0,0)) = 1
print(fn_g(1,1)) = 2
print(fn_g(2,2)) = 6
print(fn_g(4,4)) = 20
print(fn_g(8,8)) = 70
print(fn_g(16,16)) = 252


# For recursive runtime analysis of code I am trying to see (1) what the code block returns(In terms of n) You may use asymptotics(big O) if the code block return in terms of n cant be directly answered. Explain answer(2) runtime of code. Explain answer.

# For n = 2, 4, 8, 16 compute f(n).

# The number of recursive calls is doubling at each level of the tree's height. Which makes it exponentialIf the total number of nodes in a BT is The total number of nodes in a binary tree with height h is 2 ^ h - 1. So, in our case, the height of the tree is n-1, and the number of recursive calls is 2 ^ (n-1) - 1.


# When n is 1, there are no recursive calls, so it takes constant time, O(1). For any value of n greater than 1, the code block makes one recursive call with n-1 as the argument. This means that the number of recursive calls is equal to n-1. This is roughly O(~n) operations

# The loop iterates over n numbers, performing the addition operation in each iteration. Therefore, the loop has a complexity of O(n).

# For any value of n greater than 1, the code block makes two recursive calls with n//2 as the argument.
# The number of recursive calls is proportional to the height of the recursive call stack. Each recursive call reduces n by half, leading to a tree-like structure with a height of log(n)(base 2).

# The loop for adding up count iterates n times, performing a constant-time addition operation. This is O(n)
# The recursive calls are halved each time as n//2, The number of recursive calls are proportional to the height of the recursion tree, O(log(n)).
# The combined runtime is O(n log(n))
