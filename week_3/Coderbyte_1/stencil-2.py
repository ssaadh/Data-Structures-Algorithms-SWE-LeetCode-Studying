from __future__ import annotations

'''
Return the list of numbers as a string separated by space using recursion
'''
# I: [1, 2, 3]
# O: "3 "

# I: [2, 3]
# O: "2 "

# I: [3]
# O: "1 "

# Final: 1 2 3 
def recurse(lst: list[int]) -> None:
  if lst == []:
    return ""
  recursion = recurse(lst[:-1])
  last_int = str(lst[-1])
  return recursion + last_int + " "


'''
2. Calculate the factorial of N iteratively and recursively
'''
# factorial is N times product of all integers below it

# go from 1 to the value of the integer (range is  not inclusive of the stop number and requires +1)
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
3. Use binary search to find the index of a list that a certain number exists at. 
Return -1 if number does not exist. Assume that the list is sorted.
'''
def index_binary_search(lst: list[int], val: int, lo: int, hi: int):
  if lo > hi:
    return -1

  mid = (lo + hi)//2
  if lst[mid] > val:
    return index_binary_search(lst, val, lo, mid - 1)
  elif lst[mid] < val:
    return index_binary_search(lst, val, mid + 1, hi)
  elif lst[mid] == val:
    return mid

def find_index(lst: list[int], val: int) -> int:
  start = 0
  end = len(lst) - 1
  return index_binary_search(lst, val, start, end)

print(find_index([1, 5, 10, 20, 100], 5) == 1)
print(find_index([1, 5, 10, 20, 100], 15) == -1)

'''
4. Use binary search to find the index of a list that is the 
biggest number less than or equal to the given value. 
Return -1 if such a number does not exist. Assume that the list is sorted.
'''
def closest_binary_search(lst: list[int], val: int, lo: int, hi: int, last_index: int = -1):
  if lo > hi:
    return last_index  # || -1

  mid = (lo + hi)//2
  if lst[mid] > val:
    return closest_binary_search(lst, val, lo, mid - 1, last_index)
  elif lst[mid] <= val:
  # elif lst[mid] < val:
    last_index = mid
    return closest_binary_search(lst, val, mid + 1, hi, last_index)
  # elif lst[mid] == val:
    # return mid

def find_closest(lst: list[int], val: int) -> int:
  start = 0
  end = len(lst) - 1
  return closest_binary_search(lst, val, start, end)
