class Solution:
  def __init__(self, s: str, t: str) -> None:
    self.s = s
    self.t = t

  def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
      return False
    counts = [0]*26
    for c1,c2 in zip(s, t):
      barrier = ord('a')
      counts[ord(c1) - barrier] += 1
      counts[ord(c2) - barrier] -= 1
    for i in counts:
      if i != 0:
        return False
    return True

  def isAnagramSort(self, s: str, t: str) -> bool:
    # @QQ what's diff between .sort() and sorted? One returns, one is in place?
    # They'll both work in this situation, right?
    # no because it's strings right? they aren't normal iterables
    # return s.sort() == t.sort()
    return sorted(s) == sorted(t)

  # doesn't work on its own
  def isAnagramLength(self, s: str, t: str) -> bool:
    return len(s) == len(t)

sol = Solution('abc', 'cba')
print(sol.isAnagramSort('abc', 'cba'))

def selection_sort_bad_me(arr: list) -> list:
  lowest = float('inf')
  for i in range(len(arr)):
    lowest = arr[i]
    for j in range(i+1,len(arr)):
      if lowest > arr[j]:
        lowest = arr[j]
    # arr[j] = arr[i]
    # arr[i] = lowest
    arr[i], arr[j] = lowest, arr[i]
  return arr

def selection_sort(arr: list) -> list:
  lowest = float('inf')
  for i in range(len(arr)):
    lowest = arr[i]
    swap = i
    for j in range(i+1,len(arr)):
      if lowest > arr[j]:
        lowest = arr[j]
        swap = j
    arr[i], arr[swap] = arr[swap], arr[i]
  return arr

def insertion_sort(arr: list) -> list:
  for i in range(1,len(arr)):
    for j in range(i,0,-1):
      if arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
      else:
        break
  return arr

def insertionSort(n: list) -> list:
  for i in range(1, len(n)):
    current = n[i]
    j = i-1
    while (j >= 0 and current < n[j]):
      n[j+1] = n[j]
      j -= 1
    n[j+1] = current
    # print(n)
  return n

hi = selection_sort([10,6,8,4,5,1,3,7,9,2])
print(hi)
