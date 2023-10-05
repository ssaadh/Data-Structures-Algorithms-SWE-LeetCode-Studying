from __future__ import annotations
from queue import Queue
import heapq

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

'''
Suppose you’re given a list of graph edges where each edge is of the form 
("e1", "e2", 3), meaning that "e1" is connected to "e2" and has an 
edge weight of 3. The graph is connected. Write an algorithm to print 
out the an MST of the graph.

You can assume the graph is undirected for this problem. 
If there is an edge (e1, e2, 3) in the input,
you should assume there is an equivalent edge (e2, e1, 3) as well.
'''
# input = [('e1', 'e2', 6), ('e2', 'e3', 2), ('e1', 'e3', 4), ('e4', 'e5', 3), ('e1', 'e4', 5)]
# output = set([("e2", "e3", 2), ("e4", "e5" , 3), ("e1", "e3" , 4), ("e1", "e4" , 5)])

# Prim ??
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

  print(arr)
  while arr and len(res) < len(edges):
    value, parent, child = heapq.heappop(arr)
    # print(arr)

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
