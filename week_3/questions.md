## Free Response Questions

### Hashmaps



### Recursion



## Runtime Analysis 

### For each of the following code blocks, please answer the following and explain your answer choices.

# Code Block A
def fn_a(n: int) -> int:
  if n == 1:
    return n
  return fn_a(n - 1) + 1
  
  
# Code Block B
def fn_b(n: int) -> int:
  if n == 1:
    return n
  return fn_b(n - 1) + fn_b(n-1)
  
# Code Block C
def fn_c(n: int) -> int:
  if n == 1:
    return n
  return fn_c(n - 1) * n

# Code Block D
def fn_d(n: int) -> int:
  if n <= 1:
    return 1
  count = 0
  for i in range(n):
    count += i
  return fn_d(n//2) + fn_d(n // 2) + count
  
  
# Code Block E
def fn_e(n: int) -> int:
  if n == 0:
    return 1
  return fn_e(n // 2) + fn_e(n // 2)
  
# Code Block F
def fn_f(n: int) -> int:
  if n + 1 < 0:
    return n
  return fn_f(n // 2) + fn_f(n // 2)

# Code Block G
def fn_g(n: int, m: int) -> int:
    if n <= 0 or m <= 0:
        return 1
    return fn_g(n//2, m) + fn_g(n, m//2)

a. For n=2,4,8,16 compute f(n). 
b. What does the code block return? (In terms of n). Explain your answer.
c. What is the runtime of the code? Explain your answer.

