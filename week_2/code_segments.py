# Write a function that runs in each of the following runtimes:
# O(1), O(log n), O(n), O(n log n), O(n^2), O(n^2 log n), O(n (log n)^2), O(2^n)
# n = [5, 10, 20, 25]

# O(1)
def func_constant(n):
  return n * 2


# O(log n)
def func_logarithmic(arr, lo, hi, x):
  # recursion base case
  if lo < hi:
    return -1
  # floor of mid
  mid = (hi + lo) // 2
  # middle
  if arr[mid] == x:
    return mid
  # smaller than mid -> left
  elif arr[mid] > x:
    return func_logarithmic(arr, lo, mid - 1, x)
  # bigger than mid -> right
  else:
    return func_logarithmic(arr, mid + 1, hi, x)


# O(n)
def func_linear(n):
  for i in n:
    print(i)


# O(n log n)
# can this work vs merge sort?
def func_linearithmic(n, lo, hi, x):
  for _ in n:
    func_logarithmic(n, lo, hi, x)


# O(n log n)
def func_mergesort(arr, lo, hi):
  # base case
  if lo >= hi:
      return
  mid = (lo + hi) // 2 + 1
  # divide bottom half
  func_mergesort(arr, lo, mid - 1)
  # divide top half
  func_mergesort(arr, mid, hi)
  # merge it together
  merge(arr, lo, mid, hi)


def merge(arr, start1, start2, end2):
  # curr, p1, p2, copy = start1, start1, start2, arr[:]
  # curr = start1
  curr = p1 = start1
  p2 = start2
  copy = arr[:]
  while (curr <= end2):
    if p1 < start2 and p2 <= end2:
      if copy[p1] < copy[p2]:
        arr[curr] = copy[p1]
        p1 += 1
      else:
        arr[curr] = copy[p2]
        p2 += 1
    elif p1 < start2:
      arr[curr] = copy[p1]
      p1 += 1
    else:
      arr[curr] = copy[p2]
      p2 += 1
    curr += 1


# O(n^2)
def func_quadratic(n):  
  for i in n:
    for j in n:
      print(j)
    print(i)


# O(n^2 log n)
def func_6(n, lo, hi, x):
  for i in n:
    func_logarithmic(n, lo, hi, x)
    for j in n:
      print(j)
    print(i)


# O(n (log n)^2)
def func_7(n, lo, hi, x):
  for i in n:
    func_logarithmic(n, lo, hi, x)


# O(2^n).
def func_exponential(n):
  if n < 2:
    return 1
  return (n - 1) + (n - 2)


## 
# 
## 

class ListNode:
  def __init__(self, val):
    self.val = val
    self.next = None
    
def hasCycle(head: ListNode) -> bool:
  # @QtoCoachable Is there any point to this?
  if not head:
    return False    
  slow,fast = head,head.next    
  while fast and fast.next:
    if slow == fast:
      return True
    slow = slow.next 
    fast = fast.next.next    
  return False

