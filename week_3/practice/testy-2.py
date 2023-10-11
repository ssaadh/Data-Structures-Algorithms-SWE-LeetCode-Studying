def iteration(lst):
  sum = 0
  for num in range(len(lst)):
    sum += lst[num]
  return sum

def recursion(lst, num):
  if num < 0:
    return 0
  return recursion(lst, num - 1) + lst[num]

def recursion1(lst):
  if len(lst) == 0:
    return 0
  return recursion1(lst[:-1]) + lst[-1]
  
  # Test
k = [4, 2, 4, 8, 16]
print(iteration(k))
print(recursion(k, len(k) - 1))
print(recursion1(k))