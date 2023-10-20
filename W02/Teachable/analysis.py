from stopwatch import Stopwatch
import random

# How to Analyze Algorithms

# Say we have sorted of list of integers. I want to know some target,x, is the list.

# [1,2,3,4,5,6,7,8] look for 3.

# Approach1: Starting from the front, continue if each number is our target.
# 1, 2, 3

# [1,2,3,4,5,6,7,8] look for 9
# 1,2,3,4,5,6,7,8 . Nope 9 is not in our list. Return False

# Approach 2: Binary Search - continue cutting the list in half until we find our target.

# [1,2,3,4,5,6,7,8] look for 3.
# 4, 2, 3. Return True

# [1,2,3,4,5,6,7,8] look for 9
# 4 6 7 8. Return False.


# Questions to answer

# 1. How long will my program take?
# 2. How much will memory will I use?

# Common orders of growth.

# Constant: O(1)
def constant_run_time(N):
	total_sum = 0
	for i in range(0, 50):
		total_sum += i
	return total_sum

# Logarithmic: O(log n)
# N    Runtime
# 2    1 
# 4    2
# 8    3
# 16   4
def log_run_time(N):
	i = 1
	total_operations = 0
	while i < N:
		total_operations += 1
		i = i * 2
	return total_operations


# Linear: O(N)
# N     Runtime
# 2	    2
# 4     4 
# 8     8 
def linear_run_time(N):
	total_operations = 0
	i = 1
	while i < N:
		total_operations += 1
		i += 1
	return total_operations

# Quadratic: O(N^2)
def quadratic_run_time(N):
	i = 1
	total_operations = 0
	while i < N:
		j = 1
		while j < N:
			total_operations += 1
			j += 1
		i += 1
	return total_operations

# Linearithmic: O(N log N)
def linearithmic_run_time(N):
	i = 1
	total_operations = 0
	while i < N:
		j = 1
		while j < N:
			j = j * 2
			total_operations += 1
		i += 1

	return total_operations


# Exponential: O(2^N)
def exponential_run_time(N):
	if N == 0:
		return 1
	total_operations = 0
	total_operations += exponential_run_time(N-1)
	total_operations += exponential_run_time(N-1)
	return total_operations


# Constant: O(1)
# Logarithmic: O(log N)
# Linear: O(N)
# Quadratic: O(N^2)
# Linearithmic: O(N log N)
# Exponential: O(2^N)


# 2 log N ~ O(log N)
# 2 log N ~ 10logN ~ 10000 log N ~ 0.0001 log N

# 50 N^2 + 10 N log N ~ O(N^2)




# Say we have sorted of list of integers. I want to know some target,x, is the list.

def approach_one(our_list, target):
	for i in range(0, len(our_list)):
		number = our_list[i]
		if number == target:
			return i
	return -1

def approach_two(our_list, lo, hi, target):
	# Check base case 
    if hi >= lo: 
        mid = lo + (hi - lo)//2
  
        # If element is present at the middle itself 
        if our_list[mid] == target: 
            return mid 
          
        # If element is smaller than mid, then it  
        # can only be present in left subarray 
        elif our_list[mid] > target: 
            return approach_two(our_list, lo, mid-1, target) 
  
        # Else the element can only be present  
        # in right subarray 
        else: 
            return approach_two(our_list, mid + 1, hi, target) 
  
    else: 
        # Element is not present in the array 
        return -1


if __name__ == "__main__":
	input_sizes = [5, 10, 20, 40]
	num_samples = 100
	for x in input_sizes:
		input_size = 2 ** x
		timer = Stopwatch()
		input_list = range(0, input_size)
		total_runtime = 0
		for i in range(0, num_samples):
			target = random.randint(0, input_size)
			approach_two(input_list, 0, input_size - 1, target)
			total_runtime += timer.elapsed_time()
		print("2 ^ " + str(x) + " : " + str(timer.elapsed_time() / num_samples))


