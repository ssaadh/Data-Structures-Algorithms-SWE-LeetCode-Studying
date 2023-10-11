# Python3 program to merge K sorted
# arrays of different arrays
 
# Function to merge two arrays
def mergeTwoArrays(l, r):
  # array to store the result
  # after merging l and r
  ret = []
 
  # variables to store the current
  # pointers for l and r
  l_in, r_in = 0, 0
 
  # loop to merge l and r using two pointer
  while l_in + r_in < len(l) + len(r):
    if (l_in != len(l) and
       (r_in == len(r) or
      l[l_in] < r[r_in])):
         
      ret.append(l[l_in])
      l_in += 1
     
    else:
      ret.append(r[r_in])
      r_in += 1
 
  return ret
 
# Function to merge all the arrays
def mergeArrays(arr):
 
  # 2D-array to store the results
  # of a step temporar ily
  arr_s = []
 
  # Loop to make pairs of arrays
  # and merge them
  while len(arr) != 1:
 
    # To clear the data of previous steps
    arr_s[:] = []
 
    for i in range(0, len(arr), 2):
      if i == len(arr) - 1:
        arr_s.append(arr[i])
 
      else:
        arr_s.append(mergeTwoArrays(arr[i],
                      arr[i + 1]))
 
    arr = arr_s[:]
 
  # Returning the required output array
  return arr[0]
 
# Driver Code
if __name__ == "__main__":
  # Input arrays
  arr = [[3, 13],
    [8, 10, 11],
    [9, 15]]
       
  # Merged sorted array
  output = mergeArrays(arr)
 
  for i in range(0, len(output)):
    print(output[i], end = " ")
