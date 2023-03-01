from __future__ import annotations

'''
Reverse a string without the built in function to do so
'''
def reverse_str(s: str) -> str:
  # O(n), O()
  stringy = []
  for i in range(len(stringy)-1,-1,-1):
    stringy.append(i)
  return ''.join(stringy)


'''
Find the most frequent substring of length n in a string. If there’s a tie, return the alphabetically smallest.
'''
# @TODO finish
def most_freq_substring(s: str, n: int) -> str:
  # sliding window right?
  # look at n length of char each loop
  # 
  # do ord for alphabetically smallest if there's a tie
  sub_dict = {}
  most_freq = 0
  # so sub_set is init as a set
  sub_set = {'a','b'}
  sub_set.clear()
  for i in range(len(s) - n):
    subs = s[i:i+n]
    sub_dict[subs] += 1
    if sub_dict[subs] >= most_freq:
      most_freq = sub_dict[subs]
      sub_set.add(subs)
  if len(sub_set) == 1:
    return sub_set.pop()
  else:
    smallest = 0
    for i in sub_set:
      total = 0
      for j in i:
        total += ord(j)

'''
What its the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”. Time complexity does not need to be optimal.
'''
def smallest_subsequence(s: str, n: int) -> str:
  # outer loop across string:
  # loop for each lowest char to n  
  total = 0
  for j in s:
    if len(total) == n:
      return total
    total += ord(j)
  pass

'''
Merge N sorted lists.

Do not just append them all and use .sort()
Think of the merge technique used in mergesort.

Example
Input: [[1, 5, 8], [0, 2, 10], [4, 8, 9]]
Output: [0, 1, 2, 4, 5, 8, 8, 9, 10]
'''

# Other idea: loop around all the arrays at each index. Sort these in a new array?
def merge_n_lists(lst: list[list[int]]) -> list[int]:
  k = len(lsts)
  if k <= 1:
    return lst[0]
  
  mid = k // 2
  lo = lst[:mid]
  hi = lst[mid:]
  left = merge_n_lists(lo)
  right = merge_n_lists(hi)
  # return merge(left, right)

# def merge(left, right):
  p1 = len(left)
  p2 = len(right)
  x = 0
  y = 0
  new_size = p1 + p2
  new_arr = [0] * new_size
  
  while p1 < x and p2 < y:
    if left[p1] <= right[p2]:
      new_arr.append(left[x])
      p1 += 1
    else:
      new_arr.append(right[y])
      p2 += 1
  while p1 < x:
    new_arr.append(left[p1])
    p1 += 1
  while p2 < y:
    new_arr.append(right[p2])
    p2 += 1
  return new_arr

''' 
Given a list of coordinates, sort them by increasing order for X values, then decreasing order for Y values
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''
def sort_tuples(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:  
  for i in range(len(lst) - 1):
    # i2 = i += 1
    i += 1
    most = 0    
    if lst[i][0] > lst[i + 1][0]:
      most = lst[i]
    lst[i], lst[i + 1] = most, lst[i]

  for i in range(len(lst) - 1):
    cur_val = lst[i]
    cur = lst[i]
    most = 0
    while cur == cur_val:
      if lst[i][1] < lst[i + 1][1]:
        most = lst[i]
    lst[i], lst[i + 1] = most, lst[i]
  return lst