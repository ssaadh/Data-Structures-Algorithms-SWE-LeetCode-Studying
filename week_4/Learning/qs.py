def quicksort_dutch_flag(A, pivot):
	left = 0
	pointer = 0
	right = len(A) - 1
	while pointer < right:
		left_val, pointer_val, right_val = intro_vals(A, left, pointer, right)
		# left_val = A[left]
		# pointer_val = A[pointer]
		# right_val = A[right]

		if pointer_val < pivot:
			A[pointer], A[left] = left_val, pointer_val
			left += 1
			pointer += 1
		elif pointer_val > pivot:
			A[pointer], A[right] = right_val, pointer_val
			right -= 1
		else:
			pointer += 1

def quicksort_3way(A, lo = 0, hi = None):
  if hi is None:
    hi = len(A) - 1
  if hi <= lo:
    return

  pivot = A[lo]
  left = lo
  right = hi
  pointer = lo
  
  while pointer <= right:
    left_val, pointer_val, right_val = intro_vals(A, left, pointer, right)

    if A[pointer] < pivot:
      print(A[pointer], ',', A[left], ',', pointer, ',', left)
      A[pointer], A[left] = left_val, pointer_val
      left += 1
      pointer += 1
      print('Left')
    elif A[pointer] > pivot:
      print(A[pointer], ',', A[right], ',', pointer, ',', right)
      A[pointer], A[right] = right_val, pointer_val
      right -= 1
      print('Right')
    else:
      pointer += 1
      print('pivot')
    print('=====')
		
  debug_qs(A, pointer, lo, left, right, hi)
  quicksort_3way(A, lo, left - 1)
  quicksort_3way(A, right + 1, hi)
  return A

# def sort_array(arr):
  # quicksort_3way(arr, 0, len(arr) - 1)
  # return arr

def intro_vals(A, left, pointer, right):
  return A[left], A[pointer], A[right]

def debug_qs(A, pointer, lo, left, right, hi):
  print(A)
  print('pointer: ', pointer, ',', A[pointer])
  print('lo: ', lo, ',', A[lo])
  print('left: ', left-1, ',', A[left-1])
  print('right: ', right+1,  ',', A[right+1])
  print('hi: ', hi,  ',', A[hi])
  print('-')

# arr = [3, 17, 1, 3, 10, 1, 2, 14, 5, 22, 5, 3, 13, 23]
arr = ['C', 'O', 'A', 'C', 'H', 'A', 'B', 'L', 'E', 'R', 'O', 'C', 'K', 'S']
print(arr)
print('-- --')
print(quicksort_3way(arr))

data = [3, 2, 1, 3, 3, 1, 2, 2, 3, 1, 3, 1, 3, 2]
quicksort_dutch_flag(data, 2)
print('-- --')
print(data)
