# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
    # Check base case 
    if hi >= lo: 
  
        mid = lo + (hi - lo)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, lo, mid-1, x) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return binarySearch(arr, mid + 1, hi, x) 
  
    else: 
        # Element is not present in the array 
        return -1