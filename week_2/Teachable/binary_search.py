# Returns index of x in arr if present, else -1 
def binarySearch(array, x, low, high):
  if high >= low:
    mid = low + (high - low)//2
    # If found at mid, then return it
    if array[mid] == x:
      return mid
    # Search the left half
    elif array[mid] > x:
      return binarySearch(array, x, low, mid-1)
    # Search the right half
    else:
      return binarySearch(array, x, mid + 1, high)
  else:
    return -1
