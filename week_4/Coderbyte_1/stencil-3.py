from __future__ import annotations

'''
Reverse a string without the built in function to do so
'''
def reverse_str(s: str) -> str:
  extra = []
  for k in range(len(s)-1,-1,-1):
    extra.append(s[k])
  return ''.join(extra)

'''
Find the most frequent substring of length n in a string. If there’s a tie, return the alphabetically smallest.
'''
# start with the first n characters
# move across the string one at a time
# Put every substring into a dictionary or increment the dict

# to do the looping, check while the window of what youre checking out, the cut off is not greater than the length of the string
# this lets the code end correctly without it trying to compare indexes past the string length

# pull out the substrings which have the maximum count
# create an array with the current substring if its count is greater than the current max count
# otherwise add it to the array

# for alphabetically smallest, should i compare each of the letters ??
# Assuming smallest means letter by letter, "ad" is smaller than "da".
# min is a built-in function

def most_freq_substring(s: str, n: int) -> str:
  the_dict = {}
  the_slice = n
  while the_slice < len(s) + 1:
    piece = s[the_slice-n:the_slice]
    if piece in the_dict:
      the_dict[piece] += 1
    else:
      the_dict[piece] = 1
    the_slice += 1
  
  max_count = 0
  winners = []
  for substring,count in the_dict.items():
    if count > max_count:
      winners = [substring]
      max_count = count
    elif count == max_count:
      winners.append(substring)
  
  if len(winners) == 1:
    return winners[0]
  
  return(min(winners))


'''
What is the alphabetically smallest subsequence of length n in a string? 
For example, a string “agbf” and length 2 subsequence would be “ab”. Time complexity does not need to be optimal.
'''
# do the subproblem n times
# First solve for getting the smallest character from exisiting available characters
# the subproblem for finding the next smallest character:
# find the smallest letter then cut off the rest of the string (can slice) from being checked again from that stop
# same code will repeat with a smaller remaining amount of the string
# each loop will go thru ever letter and cut off from the first smallest character
# only check if character is less than. Aka not "greedy"

# the subproblem loops through a string. Have that string be modified to cut off where the smallest character is taken from
# Keep track of each 

def smallest_subsequence(s: str, n: int) -> str:
  subsequence = []
  for k in range(n):
    # sub problem begins
    min_ord = 999
    min_index = 0
    for index,char in enumerate(s):
      if ord(char) < min_ord:
        min_ord = ord(char)
        min_index = index
    # sub problem ends
    subsequence.append(s[min_index])
    s = s[min_index+1:]
  return ''.join(subsequence)


'''
Merge N sorted lists.

Do not just append them all and use .sort()
Think of the merge technique used in mergesort.

Example
Input: [[1, 5, 8], [0, 2, 10], [4, 8, 9]]
Output: [0, 1, 2, 4, 5, 8, 8, 9, 10]
'''
def merge_n_lists(lst: list[list[int]]) -> list[int]:
  if len(lst) == 1:
    return lst[0]
  return divide(lst, 0, len(lst) - 1)
  
def divide(arr, lo, hi):
  if lo >= hi:
    return arr[lo]
  mid = (lo + hi) // 2
  L = divide(arr, lo, mid)
  R = divide(arr, mid + 1, hi)
  return merge(L, R)

def merge(L: list[int], R: list[int]) -> list[int]:
  # extra space for array of size L+R
  extra = []
  # first pointer and end of left array
  p1 = 0
  end1 = len(L)
  # second pointer and end of right array
  p2 = 0
  end2 = len(R)
  # overall pointers though they aren't necessary
  pointer = 0
  total = end1 + end2

  # the same as normal mergesort
  while pointer <= total:
    if p1 < end1 and p2 < end2:
      if L[p1] < R[p2]:
        extra.append(L[p1])
        p1 += 1
      else:
        extra.append(R[p2])
        p2 += 1
    elif p1 < end1:
      extra.append(L[p1])
      p1 += 1
    elif p2 < end2:
      extra.append(R[p2])
      p2 += 1
    # increment every time for overall pointer
    pointer += 1
  return extra


''' 
Given a list of coordinates, sort them by increasing order for X values, then decreasing order for Y values
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''
# Can do any sort where the structure of the overall sorting remains how it is like insertion sort
# for the Y values, stable sorts like insertion sort already keeps relative order
# if the X value is less than Y value, then swap them. With insertion sort, check to see if the more left value is less than the right one. Swap if so.
# otherwise if X values are equal, check to see if the left Y value is greater than the right Y value. If so, swap them
# Refer to insertion sort algo for the details of how to structure the outer and inner loop
# outer loop: Go through the loop starting from the 1st index, not 0 because the inner loop swapping will compare with what has already been sorted
# the first element cant sort itself so start with the 2nd element (index 1). Index 1 will compare with index 0.
# then during the next outer loop, index 3 compares to index 2 and keep going if index 3 does a swap
# inner loop: go backwards starting from the outer loop value
# In any situation where the if statements dont work, stop the inner loop since there isnt going to be any more swapping for this

def sort_tuples(lst: list[tuple[int, int]]) -> list[tuple[int, int]]:
  for outer_loop in range(1, len(lst)):
    for inner_loop in range(outer_loop, 0, -1):
      left = lst[inner_loop]
      right = lst[inner_loop - 1]
      if left[0] < right[0]:
        lst[inner_loop], lst[inner_loop -
                             1] = lst[inner_loop - 1], lst[inner_loop]
      elif left[0] == right[0]:
        if left[1] > right[1]:
          lst[inner_loop], lst[inner_loop - 1] = lst[inner_loop - 1], lst[inner_loop]
        else:
          break
      else:
        break
  return lst
