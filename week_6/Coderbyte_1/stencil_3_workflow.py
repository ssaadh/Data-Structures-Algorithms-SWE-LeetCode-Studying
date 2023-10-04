from queue import Queue

# Going through the example input completely manually:

# [0, 1]
# 1 cant be done until 0 is done

# [1, 2]
# 2 cant be done until 1 is done

# [0, 2]
# 2 cant be done until 0 is done

# [1, 3]
# 3 cant be done until 1 is done

# [2, 3]
# 3 cant be done until 2 is done

# --

# Having the total number of courses lets us create data structures to track the courses.
# We create an inbound and outbound array. Initialize the inbound as an n length array with all 0s. Init the outbound array as an n length array with each item being an array.
# For the inbound array, we go thru the input and for the 2nd course, do +1 for that index.
# For the outbound array, go thru the input and add the 2nd course into the 1st course's array in its index.

# From the example input we would have:
# inbound: [0, 1, 2, 2]
# outbound: [[1, 2], [2, 3], [3], []]

# Init a queue. Go thru the inbound array and queue up any indexes that are 0.
# _Also have a result array and add any 0 ones to it?_
# Another loop while the queue is not empty. 
# Pop off current course from queue. Go thru its outbound index and subtract 1 from each of the courses inbound count.
# Inside the loop, check if the inbound value is now 0, add the course to the queue and add the course to the result array.
#   Should return None if there is still any inbound that isnt 0. If nothing else, run another loop through the inbound checking if any are not 0.
#   Or have a counter and for each thing added to the result, iterate the counter. If the counter is less not n-1 at the end, return None.
#   Or check the result array length. If it isn't n - 1 length, return None.
# Outside the loop, return the result.

# For course 0, this means subtracting 1 from the inbound for 1 and 2.
# inbound: [0, 0, 1, 2]
# Add course 1 to the result and the queue.

# Then course 1 is next. Subtract 1 from 2 and 3:
# inbound: [0, 0, 0, 1]
# Add course 2 to the result and the queue.

# Then for course 2, subtract 1 from 3.
# inbound: [0, 0, 0, 0]
# Add course 3 to the result and the queue.

# Then for course 3, no outbound to loop through, the loop is finished.

'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''
# input = [[0, 1], [1, 2], [0, 2], [1, 3],[2, 3]], 4
# output = [0, 1, 2, 3]
# topological sort
def find_valid_course_ordering_if_exists(prerequisites: list[list[int]], n: int) -> list[int] | None:
  inbound = [0] * n
  outbound = [[] for _ in range(n)]

  for first,second in prerequisites:
    inbound[second] += 1
    outbound[first].append(second)

  queue = Queue()
  res = []
  for index,course in enumerate(inbound):
    if course == 0:
      queue.put(index)
      res.append(index)
  
  # why does this not work if i do `while queue`
  while not queue.empty():
    curr = queue.get()
    for course in outbound[curr]:
      inbound[course] -= 1
      if inbound[course] == 0:
        queue.put(course)
        res.append(course)
  
  if len(res) == n:
    return res
  return None
  
print(find_valid_course_ordering_if_exists([[0, 1], [1, 2], [0, 2], [1, 3],[2, 3]], 4))
