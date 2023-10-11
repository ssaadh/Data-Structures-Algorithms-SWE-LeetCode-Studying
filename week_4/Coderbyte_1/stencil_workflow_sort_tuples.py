''' 
Given a list of coordinates, sort them by increasing order for X values, then decreasing order for Y values
Example
Input: [(1,1), (2,2), (2,1), (1,2)]
Output: [(1,2), (1,1), (2,2), (2,1)]
'''

'''
Input: [(1,1), (2,2), (2,1), (1,2)]

X sorted:
Middle: [(1,1), (1,2), (2,2), (2,1)]

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

def sort_tuples(lst: list) -> list:
  for outer_loop in range(1,len(lst)):
    for inner_loop in range(outer_loop, 0, -1):
      left = lst[inner_loop]
      right = lst[inner_loop - 1]
      if left[0] < right[0]:
        lst[inner_loop], lst[inner_loop - 1] = lst[inner_loop - 1], lst[inner_loop]
      elif left[0] == right[0]:
        if left[1] > right[1]:
          lst[inner_loop], lst[inner_loop - 1] = lst[inner_loop - 1], lst[inner_loop]
        else:
          break
      else:
        break
  return lst

sort_tuples([(1,1), (2,2), (2,1), (1,2)]) == [(1,2), (1,1), (2,2), (2,1)]
