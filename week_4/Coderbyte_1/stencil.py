from __future__ import annotations

'''
Reverse a string without the built in function to do so
'''
def reverse_str(s: str) -> str:
  pass

'''
Find the most frequent substring of length n in a string. If there’s a tie, return the alphabetically smallest.
'''
def most_freq_substring(s: str, n: int) -> str:
  pass

'''
What is the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”. Time complexity does not need to be optimal.
'''
def smallest_subsequence(s: str, n: int) -> str:
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