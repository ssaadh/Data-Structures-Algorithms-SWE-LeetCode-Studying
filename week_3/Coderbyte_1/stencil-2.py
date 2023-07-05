from __future__ import annotations

'''
Return the list of numbers as a string separated by space using recursion
'''
# recurse([1, 2, 3]) == "1 2 3 "

# I: [1, 2, 3]
# O: "1"

# I: [2, 3]
# O: "2"

# I: [3]
# O: "3"

# 1 2 3 

def recurse(lst: list[int]) -> str:
  if not lst:
    return ''
  
  single_el = str(lst[:1][0]) + " "
  result = recurse(lst[1:])
  return single_el + result

  
'''
2. Calculate the factorial of N iteratively and recursively
'''
# factorial is N times product of all integers below it

# go from 1 to the value of the integer (range is usually not inclusive for the end and requires +1)
# multiple a variable by the current loop counter
# return
def fact_iter(n: int) -> int:
  total = 1
  for k in range(1,n + 1):
    total *= k
  return total


# base case is to return when factorial is the lowest it should go: to 1
# pass in n - 1 and multiple by n to multiply n by each integer smaller than it
def fact_recursive(n: int) -> int:
  if n == 1:
    return 1
  result = fact_recursive(n-1)
  return result * n
  


'''
Return -1 if number does not exist. Assume that the list is sorted.
Use binary search to find the index of a list:
'''

'''
3. that a certain number exists at. 
'''
def binary_search(lst, val, lo, hi):
  if lo >= hi:
    return -1

  mid = (lo + hi)//2
  if lst[mid] > val:
    return binary_search(lst, val, lo, mid)
  elif lst[mid] < val:
    return binary_search(lst, val, mid+1, hi)
  else:
    return mid

def find_index(lst: list[int], val: int) -> int:
  start = 0
  end = len(lst) - 1
  return binary_search(lst, val, start, end)


'''
4. that is the biggest number less than or equal to the given value. 
'''
def bs(lst, val, lo, hi, last_index = -1):
  if lo > hi:
    return last_index # || -1

  mid = (lo + hi)//2
  if lst[mid] > val:
    return bs(lst, val, lo, mid-1, last_index)
  elif lst[mid] <= val:
    last_index = mid
    return bs(lst, val, mid+1, hi, last_index)

def find_closest(lst: list[int], val: int) -> int:
  start = 0
  end = len(lst) - 1
  return bs(lst, val, start, end)


print(find_closest([1, 5, 10, 20, 100], 9) == 1)
print(find_closest([1, 5, 10, 20, 100], 9))
print(find_closest([1, 5, 10, 20, 100], 21) == 3)
print(find_closest([1, 5, 10, 20, 100], 21))
print(find_closest([1, 5, 10, 20, 100], 0) == -1)
