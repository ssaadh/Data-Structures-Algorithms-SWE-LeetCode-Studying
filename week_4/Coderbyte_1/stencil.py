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
def most_freq_substring(s: str, n: int) -> str:
  # sliding window right?
  # look at n length of char each loop
  # 
  # do ord for alphabetically smallest if there's a tie
  sub_dict = {}
  most_freq = 0
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
What is the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”. Time complexity does not need to be optimal.
'''
def smallest_subsequence(s: str, n: int) -> str:
  # outer loop across string:
  # loop for each lowest char to n  
  total = 0
  for j in s:
    for i in range(n):
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
def merge_n_lists(lst: list[list[int]]) -> list[int]:
  pass

''' 
Given a list of coordinates, sort them by increasing order for X values, then decreasing order for Y values
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''
def sort_tuples(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
  pass