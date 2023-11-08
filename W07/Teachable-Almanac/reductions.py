# Given an array of integers, see if any triple sums to 0.

# nums = [-4,2,5,-1,2], return True
# nums = [-4,2,6,-1,100], return False
nums = [-20,-10,-9,-4,-2,1,1,4,5,6,7,8,29,30]        


# Solves 2SUM in O(n log n) runtime.
def two_sum(nums, targetSum = 0):
    # Sort the array first. O(n log n)
    nums.sort()

    # Now use a two pointer approach to solve 2SUM.
    i = 0
    j = len(nums) - 1
    while i < j:
        if (nums[i] + nums[j]) < targetSum:
            i += 1
        elif (nums[i] + nums[j]) > targetSum:
            j -= 1
        else: 
            return True
    return False


# With sorting and two pointer solution is O(n log n) time and O(1) space.
# Returns True if any two numbers can sum to targetSum. False otherwise.
def two_sum_non_sorted(nums, targetSum = 0):
    nums.sort() # O(n log n)
    return two_sum_sorted(nums, targetSum)

# Will solve 2SUM, assuming nums is sorted.
# O(n) runtime because we iterate with 2 pointers.
def two_sum_sorted(nums, targetSum = 0):
    if len(nums) == 0:
        return False
    
    # Now use a two pointer approach to solve 2SUM.
    i = 0
    j = len(nums) - 1
    while i < j:
        if (nums[i] + nums[j]) < targetSum:
            i += 1
        elif (nums[i] + nums[j]) > targetSum:
            j -= 1
        else: 
            return True
    return False

print(two_sum(nums))
    

def three_sum_brute(nums, targetSum = 0):
    N = len(nums)
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if i + j + k == targetSum:
                    return True
    return False


# O(n^2), O(n) space 
# Uses a hashmap to store complements.
def three_sum(nums, targetSum = 0):
    key_values = {}
    for i in range(0, len(nums)):
        x = nums[i]
        key_values[-1*x] = i
    for i, x in enumerate(nums):
        for j,y in enumerate(nums):
            if (x+y) in key_values:
                k = key_values.get(x+y) 
                if i != k and j!= k:
                    return True
    return False



# O(n^2) runtime, O(1) space.
def three_sum_sort(nums, targetSum = 0):
    nums.sort() # O(n log n) time.
    
    
    # For loop runs O(n) time
    for i,x in enumerate(nums):
        # This function runs O(n) time
        result = two_sum_sorted(nums[i+1:], -1*x)
        if result:
            return result
    return False
