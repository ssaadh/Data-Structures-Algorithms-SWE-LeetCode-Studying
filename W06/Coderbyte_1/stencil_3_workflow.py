from queue import Queue
import heapq

# input = [[0, 1], [1, 2], [0, 2], [1, 3],[2, 3]], 4
# output = [0, 1, 2, 3]
# topological sort
'''
Given a list of course prerequisites each in the form [0, 1] 
where 0 is a prerequisite of 1 and n, the total number of courses, 
write a function to output a valid course ordering, 
or None if not possible. Courses are numbered from 0 to n-1.
'''
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
  
  # why does this not work if i do `while queue`?
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


# input = [('e1', 'e2', 6), ('e2', 'e3', 2), ('e1', 'e3', 4), ('e4', 'e5', 3), ('e1', 'e4', 5)]
# output = set([("e2", "e3", 2), ("e4", "e5" , 3), ("e1", "e3" , 4), ("e1", "e4" , 5)])
'''
Suppose you’re given a list of graph edges where each edge is of the form 
("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an 
edge weight of 3. The graph is connected. Write an algorithm to print 
out the an MST of the graph.

You can assume the graph is undirected for this problem. 
If there is an edge (e1, e2, 3) in the input,
you should assume there is an equivalent edge (e2, e1, 3) as well.
'''

# Will need to rearrange the data to be able to go thru each vertex and see the smallest connection.

# If we do an adj list:
# e1: [(e2, 6), (e3, 4), (e4, 5)]
# e2: [(e1, 6), (e3, 2)]
# e3: [(e1, 4), (e2, 2)]
# e4: [(e1, 5), (e5, 3)]
# e5: [(e4, 3)]

# View of the graph
# e4 <3> e5
# |5
# e1 <6> e2 
#  \4   /2
#    e3

# Okay so it makes sense to use a PQ.
# _Go thru last PQ lecture again_

# start at e1.
# visited = [e1]

# _smallest weight is (e3, 4). PQ pulls it out_
# PQ: (e1, e2, 6), (e1, e3, 4), (e1, e4, 5)
# visited = [e1, e3]
# final: [(e1, e3, 4)]

# Add anything from e3 that isnt in PQ. Can check visited to see that the e1, one, shouldnt be added?
# PQ: (e1, e2, 6), (e1, e4, 5), (e2, e3, 2)
# _smallest weight is (e2, e3, 2). PQ pulls it out_
# visited = [e1, e2, e3]
# final = [(e1, e3, 4), (e2, e3, 2)]

# Add anything from e2 that isnt in PQ. Check visited and both e1 and 3 have been added.
# PQ: (e1, e2, 6), (e1, e4, 5)
# _smallest weight is (e1, e4, 5). PQ pulls it out_
# visited = [e1, e2, e3, e4]
# final = [(e1, e3, 4), (e2, e3, 2), (e1, e4, 5)]

# Add anything from e4 into PQ. e1 is already visited. Add e5 connection
# PQ: (e1, e2, 6), (e4, e5, 3)
# _smallest weight is (e4, e5, 3), pull it out_
# visited = [e1, e2, e3, e4, e5]
# final = [(e1, e3, 4), (e2, e3, 2), (e1, e4, 5), (e4, e5, 3)]

# Add anything from e5. Nothing.
# PQ: (e1, e2, 6)
# Pull out (e1, e2, 6). Which vertex is being checked for it already visited?
# Both are already visited.
# Done.

# --

# Create an adj list from the input. Edges are both directions. Always include the adj list current vertex first. The format should be (value, curr_vertex, connecting_vertex).
# Create a visited set, a PQ (heapq) arr, and a final array of tuples (?).
                                                                 
# Start with any vertex so we'll do input[0][1]. Go thru the adjacent vertices for the first vertex and add them to the heapq. The heapq should include both vertices and the value first so the value can be compared.

# Add input[0][1] to visited.

# How to deal with the duplicate other way around edges? In the above trace I assumed the smallest vertex always is first but can always do parent or the key and then the child vertex. When adding the next smallest edge to the final result, check to see which is smaller and add it to the set. Sets only have unique values.

# Do a while heapq or while length of the result is less than len(edges)
# heappop the smallest value. Loop through the adj list of the second/child vertex. If the last/child vertex isn't in visited, add the tuple to the heap. Outside of this neighbor checking, check if the second/child vertex is in visited. If so, go to the next iteration. We don't want to do anything else. Otherwise:
# Add the second/child vertex to visited. Finally add the tuple to the result array but the order has to be changed.
# Check which vertex is smaller and have that one be added first. Then the other vertex then the value. This is for the output.

# Added info: The "fringe" vertex can always be the second value. That will let us check that in the visited. We already know the first value is in visited since we add it that way. That's the vertex we are connecting to for the mst and removing as a fringe vertex and adding to visited.

# That's it. Outside of the loop, return the result
# ('e1', 'e2', 6), ('e2', 'e3', 2), ('e1', 'e3', 4), ('e4', 'e5', 3), ('e1', 'e4', 5)
# Prim

def output_mst(edges: list[tuple[str, str, int]]) -> list[tuple[str, str, int]]:
  adj_list = dict()
  for parent, child, value in edges:
    if parent not in adj_list:
      adj_list[parent] = [(value, parent, child)]
    else:
      adj_list[parent].append((value, parent, child))
    
    if child not in adj_list:
      adj_list[child] = [(value, child, parent)]
    else:
      adj_list[child].append((value, child, parent))

  visited = set()
  arr = []
  res = []

  starting = edges[0][0]

  visited.add(starting)
  for k in adj_list[starting]:
    heapq.heappush(arr, k)

  while arr and len(res) < len(edges):
    value, parent, child = heapq.heappop(arr)

    for val, par, chi in adj_list[child]:
      if chi not in visited:
        heapq.heappush(arr, (val, par, chi))

    if child in visited:
      continue
    else:
      visited.add(child)
    
    if int(parent[1:]) < int(child[1:]):
      res.append((parent, child, value))
    else:
      res.append((child, parent, value))
  
  return res
