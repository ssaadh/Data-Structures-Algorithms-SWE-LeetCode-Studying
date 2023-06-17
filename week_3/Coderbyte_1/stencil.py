from __future__ import annotations
sleep
'''
Return the list of numbers as a string separated by space using recursion
'''
def recurse(lst: list[int]) -> None:
  new_lst = []
  for i in lst:
    new_lst.append(str(i) + ' ')
  return ''.join(new_lst)



'''
2. Calculate the factorial of N iteratively and recursively
'''
def fact_iter(n: int) -> int:
  num = 1
  for i in range(1, n+1):
    num *= i
  return num

def fact_recursive(n: int) -> int:
  if n == 0:
    return 1
  else:
    return n * fact_recursive(n-1)
    

'''
3. Use binary search to find the index of a list that a certain number exists at. 
Return -1 if number does not exist. Assume that the list is sorted.
'''
def find_index(lst: list[int], val: int) -> int:
  lo = 0
  hi = len(lst) - 1
  while lo <= hi:
    mid = (lo+hi) // 2
    if lst[mid] == val:
      return mid
    elif lst[mid] < val:
      lo = mid+1
    else:
      hi = mid-1
  return -1


'''
4. Use binary search to find the index of a list that is the 
biggest number less than or equal to the given value. 
Return -1 if such a number does not exist. Assume that the list is sorted.
'''
def find_closest(lst: list[int], val: int) -> int:
  lo = 0
  hi = len(lst) - 1
  while lo <= hi:
    mid = (lo+hi) // 2
    if lst[mid] == val:
      return mid
    elif lst[mid] < val:
      lo = mid+1
    else:
      hi = mid-1
  # diff
  return lo-1 or -1
