def quicksort_3way_debug(arr, low, high):
  if high <= low:
    return

  lt = low
  gt = high
  pivot = arr[low]
  i = low

  if low == 0 and lt == 0 and i == 0 and gt == len(arr) - 1:
    print(arr)
    print('-')
  while i <= gt:
    if arr[i] < pivot:
      arr[i], arr[lt] = arr[lt], arr[i]
      lt += 1
      i += 1
      print('1st')
    elif arr[i] > pivot:
      arr[i], arr[gt] = arr[gt], arr[i]
      gt -= 1
      print('2nd')
    else:
      i += 1
      print('3rd')
  print(arr)
  print('i: ', i)
  print('low: ', low)
  print('lt: ', lt-1)
  print('gt: ', gt+1)
  print('high: ', high)
  print('---')
  quicksort_3way(arr, low, lt - 1)
  quicksort_3way(arr, gt + 1, high)

def quicksort_3way(arr, low, high):
  if high <= low:
    return

  lt = low
  gt = high
  pivot = arr[low]
  i = low

  while i <= gt:
    if arr[i] < pivot:
      arr[i], arr[lt] = arr[lt], arr[i]
      lt += 1
      i += 1
    elif arr[i] > pivot:
      arr[i], arr[gt] = arr[gt], arr[i]
      gt -= 1
    else:
      i += 1
  
  quicksort_3way(arr, low, lt - 1)
  quicksort_3way(arr, gt + 1, high)

def sort_array(arr):
  quicksort_3way(arr, 0, len(arr) - 1)
  return arr

def samp(A, mid):
    i = 0
    j = 0
    k = len(A)
    while j < k:
        if A[j] < mid:
            A[i], A[j] = A[j], A[i]
            i = i + 1
            j = j + 1
        elif A[j] > mid:
            k = k - 1
            A[j], A[k] = A[k], A[j]
        else:
            j = j + 1
        
from random import shuffle
data = [1,2,3]*10
shuffle(data)

samp(data, 2)

# Testing the function
# arr = [25, 3, 19, 8, 12, 3, 5, 19, 8]
# print(sort_array(arr))

arr = [3, 17, 1, 3, 10, 1, 2, 14, 5, 22, 5, 3, 13, 23]
print(sort_array(arr))
arr2 = [3, 17, 1, 3, 10, 1, 2, 14, 5, 22, 5, 3, 13, 23]
quicksort_3way(arr2, 0, len(arr) - 1)
print(arr2)
